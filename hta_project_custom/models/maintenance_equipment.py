# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MaintenanceEquipement(models.Model):
    _inherit = "maintenance.equipment"
    
    project_task_id = fields.Many2one('project.task', string="Task", ondelete="cascade")