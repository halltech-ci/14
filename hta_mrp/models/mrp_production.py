# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class MrpProduction(models.Model):
    _inherit = "mrp.production"
    
    sale_order_id = fields.Many2one('sale.order', string="Commande", domain="[('state', '=', 'sale')]")
    description = fields.Text("Description")
    mrp_order_line_ids = fields.One2many(related="sale_order_id.order_line", string="Order line")
    
    @api.onchange('sale_order_id')
    def _onchange_sale_order(self):
        if not self.bom_id and self.sale_order_id.sale_mrp_product:
            self.product_id = self.sale_order_id.sale_mrp_product
            self.product_qty = 1.0
            
    @api.constrains('move_raw_ids', 'mrp_order_line_ids')
    def _check_product_qty(self):
        for product in self:
            if product.mrp_order_line_ids.product_id:
                if product.move_raw_ids.product_uom_qty > product.mrp_order_line_ids.product_uom_qty:
                    raise ValidationError(_('Quantity of {0} can not be greather than{1}'.format(product.move_raw_ids.product_id.name, product.mrp_order_line_ids.product_uom_qty)))
