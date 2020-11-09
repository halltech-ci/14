# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    sale_mrp_product = fields.Many2one('product.product', ondelete='cascade')
    mo_id = fields.Many2one('mrp.production', ondelete='cascade', string="Manufacturing Order")
    
    """
    Create BOM associated to the SO. 
    """
    def create_sale_mrp_product(self):
        '''create product template for coresponding sale_order'''
        product_product = self.env['product.product']
        manufacture_order = self.env['mrp.production']
        for order in self:
            if not order.sale_mrp_product and order.description:
                product_name = order.description
                route_id = self.env['stock.location.route'].search([('name', '=', 'Manufacture')]).id
                route = []
                route_ids = route.append(route_id)
                product_prod = product_product.create({
                    'name': product_name,
                    'type': 'product',
                    'purchase_ok': False,
                    'categ_id': 1,
                    'route_ids': route_ids
                })
            order.sale_mrp_product = product_prod
            if not order.mo_id:
                manufacture_order.create({
                    'product_id': order.sale_mrp_product,
                    'mrp_order_line_ids': order.order_line
                })
            
            
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    in_mrp_line = fields.Boolean(string="MRP line", default=True)
    mrp_production_id = fields.Many2one('mrp.production')