# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    secondary_uom_ids = fields.One2many(
        comodel_name="product.secondary.unit",
        inverse_name="product_tmpl_id",
        string="Secondary Unit of Measure",
        help="Default Secondary Unit of Measure.",
    )
    type = fields.Selection(default='service')

class ProductSecondaryUnit(models.Model):
    _name = "product.secondary.unit"
    _description = "Product Secondary Unit"

    name = fields.Char(required=True, translate=True)
    code = fields.Char()
    product_tmpl_id = fields.Many2one(
        comodel_name="product.template",
        string="Product Template",
        required=True,
        ondelete="cascade",
    )
    uom_id = fields.Many2one(
        comodel_name="uom.uom",
        string="Secondary Unit of Measure",
        required=True,
        help="Default Secondary Unit of Measure.",
    )
    factor = fields.Float(
        string="Secondary Unit Factor", default=1.0, digits=0, required=True
    )

    def name_get(self):
        result = []
        for unit in self:
            result.append(
                (
                    unit.id,
                    "{unit_name}-{factor}".format(
                        unit_name=unit.name, factor=unit.factor
                    ),
                )
            )
        return result

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        if args is None:
            args = []
        units = self.search([("code", "=", name)] + args, limit=1)
        if not units:
            return super(ProductSecondaryUnit, self).name_search(
                name=name, args=args, operator=operator, limit=limit
            )
        return units.name_get()