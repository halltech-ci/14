# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    sale_secondary_uom_id = fields.Many2one(
        comodel_name="product.secondary.unit", 
        string="Default secondary unit for sales"
    )
    
