# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = "stock.move"
    
    product_code = fields.Char(string="Code", related="product_id.default_code")