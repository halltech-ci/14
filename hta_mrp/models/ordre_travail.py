# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OrderTravail(models.Model):
    _name = "ordre.travail"
    
    name = fields.Char('Reference')
    mrp_id = fields.Many2one('mrp.production', string="Manufacture Order")