# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Task(models.Model):
    """Added Product Used in the Project Task."""

    _inherit = "project.task"

    material_ids = fields.One2many(
        'project.task.material', 'task_id',
        string='Product Used')


class ProjectTaskMaterial(models.Model):
    """Added Product and Quantity in the Task Material Used."""

    _name = "project.task.material"
    _description = "Task Material Used"

    task_id = fields.Many2one(
        'project.task', string='Task', ondelete='cascade',
        required=True)
    product_id = fields.Many2one(
        'product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity')

    @api.constrains('quantity')
    def _check_quantity(self):
        for material in self:
            if not material.quantity > 0.0:
                raise ValidationError(
                    _('Quantity of material consumed must be greater than 0.')
                )
