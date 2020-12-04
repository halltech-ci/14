# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mrp_stock_request(models.Model):
#     _name = 'mrp_stock_request.mrp_stock_request'
#     _description = 'mrp_stock_request.mrp_stock_request'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
