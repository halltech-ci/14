# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'
    
    task_product_id = fields.One2many(
        'project.task.material',
        'stock_move_id',
        string='Project Task Product',
    )

    def _action_done(self, cancel_backorder=False):
        # The analytical amount is updated with the value of the
        # stock movement, because if the product has a tracking by
        # lot / serial number, the cost when creating the
        # analytical line is not correct.
        res = super(StockMove, self)._action_done()
        self.mapped('task_product_id')._update_unit_amount()
        return res