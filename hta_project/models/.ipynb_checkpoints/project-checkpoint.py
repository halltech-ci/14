from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Task(models.Model):
    """Added Material Used in the Project Task."""

    _inherit = "project.task"

    product_ids = fields.One2many(
        comodel_name="project.task.product",
        inverse_name="task_id",
        string="Product Used",
    )


class ProjectTaskProduct(models.Model):
    """Added Product and Quantity in the Task Material Used."""

    _name = "project.task.product"
    _description = "Task product Used"

    task_id = fields.Many2one(
        comodel_name="project.task", string="Task", ondelete="cascade", required=True
    )
    product_id = fields.Many2one(
        comodel_name="product.product", string="Product", required=True
    )
    product_code = fields.Char(related="product_id.default_code")
    quantity = fields.Float(string="Quantity")

    @api.constrains("quantity")
    def _check_quantity(self):
        for material in self:
            if not material.quantity > 0.0:
                raise ValidationError(
                    _("Quantity of material consumed must be greater than 0.")
                )