# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    location_source_id = fields.Many2one(
        'stock.location',
        string='Source Location',
        index=True,
        help='Default location from which materials are consumed.',
    )
    location_dest_id = fields.Many2one(
        'stock.location',
        string='Destination Location',
        index=True,
        help='Default location to which materials are consumed.',
    )