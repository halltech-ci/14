# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    
    secondary_uom_ids = fields.One2many(
        comodel_name="product.secondary.unit",
        inverse_name="product_tmpl_id",
        string="Secondary Unit of Measure",
        help="Default Secondary Unit of Measure.",
    )
    sale_secondary_uom_id = fields.Many2one(
        comodel_name="product.secondary.unit", 
        string="Default secondary unit for sales"
    )
    
