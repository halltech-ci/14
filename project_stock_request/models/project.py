# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _inherit = 'project.project'

    stock_request_order_ids = fields.One2many('stock.request.order',
                                              'project_id',
                                              string='Stock Request Orders')
