# -*- coding: utf-8 -*-

from odoo import models, fields, api

 
class HrPayslipWorkedDays(models.Model):
    _inherit = 'hr.payslip.worked_days'

    imported_from_leave = fields.Boolean(
        string='Imported From Leave',
        default=False
    )

class HrPayslipWorkedDaysOvertime(models.Model):
    _inherit = 'hr.payslip.worked_days'

    imported_from_overtime = fields.Boolean(
        string='Imported From Overtime',
        default=False
    )

    
class HrWorkEntryType(models.Model):
    _inherit = 'hr.work.entry.type'
    
    is_overtime = fields.Boolean(string="Is Overtime", store=True, default=False)
    
    overtime_ids = fields.One2many(comodel_name ="bt.hr.overtime", inverse_name ="work_entry_type_id", string = "All Overtimes",store=True )

    
class HrWorkEntry(models.Model):
    _inherit = 'hr.work.entry'
    
    overtime_id = fields.Many2one('bt.hr.overtime', string='Overtime', store=True)
    

class HrOvertime(models.Model):
    _inherit = 'bt.hr.overtime'

    work_entry_type_id = fields.Many2one('hr.work.entry.type', string='Type', help="The code that can be used in the salary rules", store=True)