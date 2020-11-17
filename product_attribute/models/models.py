# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class product_attribute(models.Model):
#     _name = 'product_attribute.product_attribute'
#     _description = 'product_attribute.product_attribute'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
