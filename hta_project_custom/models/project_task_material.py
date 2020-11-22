# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTaskMaterial(models.Model):
    """Added Product and Quantity in the Task Material Used."""

    _name = "project.task.material"
    _description = "Task Material Used"

    task_id = fields.Many2one(
        comodel_name="project.task", string="Task", ondelete="cascade", required=True
    )
    product_id = fields.Many2one(
        comodel_name="product.product", string="Product", required=True
    )
    quantity = fields.Float(string="Quantity")
    initial_qty = fields.Float(string="Initial Qty")
    qty_used = fields.Float(string="Quantity Used")
    product_code = fields.Char(related="product_id.default_code")

    @api.constrains("quantity")
    def _check_quantity(self):
        for material in self:
            if not material.quantity > 0.0:
                raise ValidationError(
                    _("Quantity of material consumed must be greater than 0.")
                )