# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _inherit = "project.project"
    
    sale_order_ids = fields.One2many("sale.order", "project_id", string="Sale Orders")