# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    consume_material = fields.Boolean(
        help="If you mark this check, when a task goes to this state, "
             "it will consume the associated materials",
    )
    

class ProjectTask(models.Model):
    _inherit = "project.task"
    
    @api.depends('material_ids.stock_move_id')
    def _compute_stock_move(self):
        for task in self:
            task.stock_move_ids = task.mapped('material_ids.stock_move_id')

    @api.depends('material_ids.analytic_line_id')
    def _compute_analytic_line(self):
        for task in self:
            task.analytic_line_ids = task.mapped(
                'material_ids.analytic_line_id')

    @api.depends('stock_move_ids.state')
    def _compute_stock_state(self):
        for task in self:
            if not task.stock_move_ids:
                task.stock_state = 'pending'
            else:
                states = task.mapped("stock_move_ids.state")
                for state in ("confirmed", "assigned", "done"):
                    if state in states:
                        task.stock_state = state
                        break

    material_ids = fields.One2many(
        comodel_name="project.task.material",
        inverse_name="task_id",
        string="Product Used",
    )
    equipment_ids = fields.One2many('equipment.equipment', "project_task_id")
    
    picking_id = fields.Many2one(
        "stock.picking",
        related="stock_move_ids.picking_id",
    )
    stock_move_ids = fields.Many2many(
        comodel_name='stock.move',
        compute='_compute_stock_move',
        store = True,
        string='Stock Moves',
    )
    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Move Analytic Account',
        help='Move created will be assigned to this analytic account',
    )
    analytic_line_ids = fields.Many2many(
        comodel_name='account.analytic.line',
        compute='_compute_analytic_line',
        store = True,
        string='Analytic Lines',
    )
    consume_material = fields.Boolean(
        related='stage_id.consume_material',
    )
    stock_state = fields.Selection(
        selection=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('assigned', 'Assigned'),
            ('done', 'Done')],
        compute='_compute_stock_state',
    )
    location_source_id = fields.Many2one(
        comodel_name='stock.location',
        string='Source Location',
        index=True,
        help='Keep this field empty to use the default value from'
        ' the project.',
    )
    location_dest_id = fields.Many2one(
        comodel_name='stock.location',
        string='Destination Location',
        index=True,
        help='Keep this field empty to use the default value from'
        ' the project.'
    )

    def unlink_stock_move(self):
        res = False
        moves = self.mapped('stock_move_ids')
        moves_done = moves.filtered(lambda r: r.state == 'done')
        if not moves_done:
            moves.filtered(lambda r: r.state == 'assigned')._do_unreserve()
            moves.filtered(
                lambda r: r.state in {'waiting', 'confirmed', 'assigned'}
            ).write({'state': 'draft'})
            res = moves.unlink()
        return res

    def write(self, vals):
        res = super(ProjectTask, self).write(vals)
        for task in self:
            if 'stage_id' in vals or 'material_ids' in vals:
                if task.consume_material:
                    todo_lines = task.material_ids.filtered(
                        lambda m: not m.stock_move_id
                    )
                    if todo_lines:
                        todo_lines.create_stock_move()
                        todo_lines.create_analytic_line()
                else:
                    if task.unlink_stock_move() and task.material_ids.mapped(
                            'analytic_line_id'):
                        raise exceptions.Warning(
                            _("You can't move to a not consume stage if "
                              "there are already analytic lines")
                        )
                    task.material_ids.mapped('analytic_line_id').unlink()
        return res

    def unlink(self):
        self.mapped('stock_move_ids').unlink()
        self.mapped('analytic_line_ids').unlink()
        return super(Task, self).unlink()

    def action_assign(self):
        self.mapped('stock_move_ids')._action_assign()

    def action_done(self):
        for move in self.mapped('stock_move_ids'):
            move.quantity_done = move.product_uom_qty
        self.mapped('stock_move_ids')._action_done()

