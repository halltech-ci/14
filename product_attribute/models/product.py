# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"
    
    def _get_default_code(self):
        return self.env["ir.sequence"].next_by_code("product.default.code")

    default_code = fields.Char(
        "Internal Reference", index=True, default=_get_default_code
    )
    
    _sql_constraints = [
        (
            "default_code_uniq",
            "unique(default_code)",
            "Internal Reference must be unique across the database!",
        )
    ]
