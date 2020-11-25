# -*- coding: utf-8 -*-


from odoo import models, fields, api


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom,
                               location_id, name, origin, values, group_id):
        result = super(StockRule, self)._get_stock_move_values(
            product_id, product_qty, product_uom,
            location_id, name, origin, values, group_id)
        if values.get('stock_request_id', False):
            result['allocation_ids'] = [(0, 0, {
                'stock_request_id': values.get('stock_request_id'),
                'requested_product_uom_qty': product_qty,
            })]
        return result