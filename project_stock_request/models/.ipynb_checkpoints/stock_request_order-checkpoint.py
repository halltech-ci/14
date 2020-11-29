# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockRequestOrder(models.Model):
    _inherit = 'stock.request.order'

    project_id = fields.Many2one('project.project', string='Project',
                                 )
    project_task_id = fields.Many2one('project.task', string='Project Task',
                                      )
