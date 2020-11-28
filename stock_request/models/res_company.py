# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    stock_request_allow_virtual_loc = fields.Boolean(
        string='Allow Virtual locations on Stock Requests',
    )
