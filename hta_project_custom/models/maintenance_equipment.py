# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MaintenanceEquipement(models.Model):
    _name = "equipment.equipment"
    _rescription = "My custom equipement"
    
    project_task_id = fields.Many2one('project.task', string="Task", ondelete="cascade")
    equipment_id = fields.Many2one('maintenance.equipment')
    equipment_category = fields.Many2one(related="equipment_id.category_id", string="Category")