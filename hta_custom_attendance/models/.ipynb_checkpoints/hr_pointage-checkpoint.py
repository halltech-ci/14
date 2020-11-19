# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    
    leave_days_line_ids = fields.One2many('hr.pointage', 'payslip_id',
        string='Payslip Leaves Days', copy=True, readonly=True,
        states={'draft': [('readonly', False)], 'verify': [('readonly', False)]})
    
    

class HrPointage(models.Model):
     _name = "hr.pointage"
    
     name = fields.Char(string='Name', readonly=True,
        states={'draft': [('readonly', False)]})
     payslip_id = fields.Many2one('hr.payslip', string='Pay Slip', required=True, ondelete='cascade', index=True)
     sequence = fields.Integer()
     code = fields.char()   
     number_of_days = fields.Float()
     number_of_hours_absentee = fields.Float()
     contract_id = fields.Many2one('hr.contract', string='Contract', readonly=True,
        states={'draft': [('readonly', False)]})
        
        
    #recupere les pointages d_un employee entre debut et fin
    @api.model
    def get_worked_days(self, debut, fin, employee):
        domain = [('employee_id', '=', employee.id), ('check_in', '>=', debut), ('check_out', '<=', fin)]
        
        domain_leave_days = [('employee_id', '=', employee.id), ('number_of_days', '!=', False)]
        
        absences_days = self.env['hr.leave'].search(domain_leave_days)
        absences_hours = self.env['hr.leave'].search(domain_leave_hours)
        attendances =  self.env['hr.attendance'].search(domain)
        hours = 0
        days = 0
        check_in_date_list = []
        check_out_date_list = []
        
        
        for attendance in attendances:
            check__in_date = attendance.check_in
            check__out_date = attendance.check_out
            
        
        for absence_day in absences_days:
            check_absence_day = absence_day.number_of_days
            check_absence_hours = absence_day.number_of_hours_display
            
            hours = hours + check_absence_hours
            days = days + check_absence_day
        self.number_of_days = days
        self.number_of_hours_absentee = hours
        check_in_date_list.append(check_absence_day)
        check_out_date_list.append(check_absence_hours)
    
    
    #--------------------------------------------------------------------------------
    