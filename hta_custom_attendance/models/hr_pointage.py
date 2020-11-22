# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    
    leave_days_line_ids = fields.One2many('hr.pointage', 'payslip_id', string='Payslip Leaves Days', copy=True, readonly=True,states={'draft': [('readonly', False)], 'verify': [('readonly', False)]})
    
    

class HrPointage(models.Model):
     _name = "hr.pointage"
    
     employee_id = fields.Many2one('hr.employee', default='')
     attendance_id = fields.Many2one()
    
     leave_id = fiels.Many2one('hr.leave', string= 'Leave id', required=True)   
     number_of_days = fields.Float(string="Nombre de jours", compute='_compute_number_days')
     number_of_hours_absentee = fields.Float(string='Nombre heures', compute='_compute_number_hours')
     contract_id = fields.Many2one('hr.contract', string='Contract', readonly=True, states={'draft': [('readonly', False)]})
        
        
    #recupere les pointages d_un employee entre debut et fin
   
    @api.depends('leave_id.number_of_hours_display')  
    def _compute_number_hours(self):
        domain = [('employee_id', '=', employee.id),]
        absences_hours = self.env['hr.leave'].search(domain)
        total_leaves_hours = 0
        for leave_hours in absences_hours: 
            total_leaves_hours += leave_hours.leave_id.number_of_hours_display
        self.number_of_hours_absentee = total_leaves_hours
    
    @api.depends('leave_id.number_of_days')  
    def _compute_number_days(self,employee):
        domain = [('employee_id', '=', employee.id), ()]
        absences_days = self.env['hr.leave'].search(domain)
        total_leaves_days = 0
        state = ['validate','validate1']
        for leave_days in absences_days: 
            if leave_days.leave_id.state in state:
                total_leaves_days += leave_days.leave_id.number_of_days 
        self.number_of_days = total_leaves_days