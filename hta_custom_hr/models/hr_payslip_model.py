# -*- coding: utf-8 -*-

from odoo import models, fields, api

 
class HrPayslipWorkedDays(models.Model):
    _inherit = 'hr.payslip.worked_days'

    imported_from_leave = fields.Boolean(
        string='Imported From Leave',
        default=False
    )
