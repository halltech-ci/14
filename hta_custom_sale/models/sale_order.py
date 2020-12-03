# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools.float_utils import float_compare, float_round

_SALE_ORDER_DOMAINE = [('fm', 'FABRICATION MECANIQUE'),
                          ('cm', 'CONSTRUCTION METALLIQUE'),
                          ('gc', 'GENIE CIVILE'),
                          ('ct', 'CHAUDRONNERIE TUYAUTERIE'),
                          ('em', 'ELECTROMECANIQUE'),
                          ('bt', 'BATIMENT'),
                          ('ra', 'RECTIFICATION AUTOMOBILE'),
                          ('mi', 'MAINTENANCE INDUSTRIELLE'),
                          ('me', 'MAINTENANCE ELECTROMECANIQUE'),
                          ('mm', 'MAINTENANCE MECANIQUE'),
                          ('cu', 'CONSTRUCTION USINE'),
                          ('ep', 'ETUDES DE PROJET')
    ]

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    description = fields.Text("Description : ")
    signed_user = fields.Many2one("res.users", string="Signed In User", readonly=True, default= lambda self: self.env.uid)
    sale_order_recipient = fields.Char("Destinataire")
    sale_order_type = fields.Selection(_SALE_ORDER_DOMAINE, string="Domaine",
                                 required=True, index=True, default='fm')
    project_id = fields.Many2one("project.project", string="Project", ondelete="cascade")
    project_key = fields.Char(string="Projet", related="project_id.key")
    
    
    """
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if vals.get('sale_order_type', 'fm'):
                domaine_code = vals.get('sale_order_type')
                next_code = '{0}.{1}.{2}'.format('sale',domaine_code, 'sequence')
                if 'company_id' in vals:
                    vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code(next_code) or _('New')
                else:
                    vals['name'] = self.env['ir.sequence'].next_by_code(next_code) or _('New')

        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        if any(f not in vals for f in ['partner_invoice_id', 'partner_shipping_id', 'pricelist_id']):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            addr = partner.address_get(['delivery', 'invoice'])
            vals['partner_invoice_id'] = vals.setdefault('partner_invoice_id', addr['invoice'])
            vals['partner_shipping_id'] = vals.setdefault('partner_shipping_id', addr['delivery'])
            vals['pricelist_id'] = vals.setdefault('pricelist_id', partner.property_product_pricelist and partner.property_product_pricelist.id)
        result = super(SaleOrder, self).create(vals)
        return result"""


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    secondary_uom_qty = fields.Float(
        string="Secondary Qty", digits="Product Unit of Measure"
    )
    secondary_uom_id = fields.Many2one(
        comodel_name="product.secondary.unit",
        string="Secondary uom",
        ondelete="restrict",
    )

    @api.onchange("secondary_uom_id", "secondary_uom_qty")
    def onchange_secondary_uom(self):
        if not self.secondary_uom_id:
            return
        factor = self.secondary_uom_id.factor * self.product_uom.factor
        qty = float_round(
            self.secondary_uom_qty * factor,
            precision_rounding=self.product_uom.rounding,
        )
        if (
            float_compare(
                self.product_uom_qty, qty, precision_rounding=self.product_uom.rounding
            )
            != 0
        ):
            self.product_uom_qty = qty

    @api.onchange("product_uom_qty")
    def onchange_secondary_unit_product_uom_qty(self):
        if not self.secondary_uom_id:
            return
        factor = self.secondary_uom_id.factor * self.product_uom.factor
        qty = float_round(
            self.product_uom_qty / (factor or 1.0),
            precision_rounding=self.secondary_uom_id.uom_id.rounding,
        )
        if (
            float_compare(
                self.secondary_uom_qty,
                qty,
                precision_rounding=self.secondary_uom_id.uom_id.rounding,
            )
            != 0
        ):
            self.secondary_uom_qty = qty

    @api.onchange("product_uom")
    def onchange_product_uom_for_secondary(self):
        if not self.secondary_uom_id:
            return
        factor = self.product_uom.factor * self.secondary_uom_id.factor
        qty = float_round(
            self.product_uom_qty / (factor or 1.0),
            precision_rounding=self.product_uom.rounding,
        )
        if (
            float_compare(
                self.secondary_uom_qty,
                qty,
                precision_rounding=self.product_uom.rounding,
            )
            != 0
        ):
            self.secondary_uom_qty = qty

    @api.onchange("product_id")
    def product_id_change(self):
        """
        If default sales secondary unit set on product, put on secondary
        quantity 1 for being the default quantity. We override this method,
        that is the one that sets by default 1 on the other quantity with that
        purpose.
        """
        res = super().product_id_change()
        self.secondary_uom_id = self.product_id.sale_secondary_uom_id
        if self.secondary_uom_id:
            self.secondary_uom_qty = 1.0
            self.onchange_secondary_uom()
        return res