# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTaskMaterial(models.Model):
    """Added Product and Quantity in the Task Material Used."""

    _name = "project.task.material"
    _description = "Task Material Used"

    task_id = fields.Many2one(
        comodel_name="project.task", string="Task", ondelete="cascade", required=True
    )
    product_id = fields.Many2one('product.product', string="Product"
        domain="[('type', 'in', ('consu', 'product'))]"
    )
    quantity = fields.Float(string="Quantity")
    initial_qty = fields.Float(string="Initial Qty")
    qty_used = fields.Float(string="Quantity Used")
    product_code = fields.Char(related="product_id.default_code")
    
    stock_move_id = fields.Many2one(
        comodel_name='stock.move',
        string='Stock Move',
    )
    analytic_line_id = fields.Many2one(
        comodel_name='account.analytic.line',
        string='Analytic Line',
    )
    product_uom_id = fields.Many2one(
        comodel_name='uom.uom',
        oldname="product_uom",
        string='Unit of Measure',
    )

    @api.constrains("quantity")
    def _check_quantity(self):
        for material in self:
            if not material.quantity > 0.0:
                raise ValidationError(
                    _("Quantity of material consumed must be greater than 0.")
                )
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        self.product_uom_id = self.product_id.uom_id.id
        return {'domain': {'product_uom_id': [
            ('category_id', '=', self.product_id.uom_id.category_id.id)]}}

    def _prepare_stock_move(self):
        product = self.product_id
        res = {
            'product_id': product.id,
            'name': product.partner_ref,
            'state': 'confirmed',
            'product_uom': self.product_uom_id.id or product.uom_id.id,
            'product_uom_qty': self.quantity,
            'origin': self.task_id.name,
            'location_id':
                self.task_id.location_source_id.id or
                self.task_id.project_id.location_source_id.id or
                self.env.ref('stock.stock_location_stock').id,
            'location_dest_id':
                self.task_id.location_dest_id.id or
                self.task_id.project_id.location_dest_id.id or
                self.env.ref('stock.stock_location_customers').id,
        }
        return res
    
    def create_stock_move(self):
        pick_type = self.env.ref(
            'project_task_material_stock.project_task_material_picking_type')
        task = self[0].task_id
        picking_id = task.picking_id or self.env['stock.picking'].create({
            'origin': "{}/{}".format(task.project_id.name, task.name),
            'partner_id': task.partner_id.id,
            'picking_type_id': pick_type.id,
            'location_id': pick_type.default_location_src_id.id,
            'location_dest_id': pick_type.default_location_dest_id.id,
        })
        for line in self:
            if not line.stock_move_id:
                move_vals = line._prepare_stock_move()
                move_vals.update({'picking_id': picking_id.id or False})
                move_id = self.env['stock.move'].create(move_vals)
                line.stock_move_id = move_id.id

    def _prepare_analytic_line(self):
        product = self.product_id
        company_id = self.env['res.company']._company_default_get(
            'account.analytic.line')
        analytic_account = getattr(self.task_id, 'analytic_account_id', False)\
            or getattr(self.task_id.project_id, 'analytic_account_id', False)
        if not analytic_account:
            raise exceptions.Warning(
                _("You must assign an analytic account for this task/project.")
            )
        res = {
            'name': self.task_id.name + ': ' + product.name,
            'ref': self.task_id.name,
            'product_id': product.id,
            'unit_amount': self.quantity,
            'account_id': analytic_account.id,
            'user_id': self._uid,
            'product_uom_id': self.product_uom_id.id,
            'company_id': analytic_account.company_id.id or
            self.env.user.company_id.id,
            'partner_id': self.task_id.partner_id.id or
            self.task_id.project_id.partner_id.id or None,
            'task_material_id': [(6, 0, [self.id])],
        }
        amount_unit = \
            self.product_id.with_context(uom=self.product_uom_id.id).price_get(
                'standard_price')[self.product_id.id]
        amount = amount_unit * self.quantity or 0.0
        result = round(amount, company_id.currency_id.decimal_places) * -1
        vals = {'amount': result}
        if 'employee_id' in self.env['account.analytic.line']._fields:
            vals['employee_id'] = \
                self.env['hr.employee'].search([
                    ('user_id', '=', self.task_id.user_id.id)
                ], limit=1).id
        res.update(vals)
        return res
    
    def create_analytic_line(self):
        for line in self:
            self.env['account.analytic.line'].create(
                line._prepare_analytic_line())

    def unlink_stock_move(self):
        if not self.stock_move_id.state == 'done':
            if self.stock_move_id.state == 'assigned':
                self.stock_move_id._do_unreserve()
            if self.stock_move_id.state in (
               'waiting', 'confirmed', 'assigned'):
                self.stock_move_id.write({'state': 'draft'})
            picking_id = self.stock_move_id.picking_id
            self.stock_move_id.unlink()
            if not picking_id.move_line_ids_without_package and \
               picking_id.state == 'draft':
                picking_id.unlink()

    def _update_unit_amount(self):
        # The analytical amount is updated with the value of the
        # stock movement, because if the product has a tracking by
        # lot / serial number, the cost when creating the
        # analytical line is not correct.
        for sel in self.filtered(lambda x: x.stock_move_id.state == 'done' and
                                 x.analytic_line_id.amount !=
                                 x.stock_move_id.value):
            sel.analytic_line_id.amount = sel.stock_move_id.value

    @api.model
    def unlink(self):
        self.unlink_stock_move()
        if self.stock_move_id:
            raise exceptions.Warning(
                _("You can't delete a consumed material if already "
                  "have stock movements done.")
            )
        self.analytic_line_id.unlink()
        return super(ProjectTaskMaterial, self).unlink()