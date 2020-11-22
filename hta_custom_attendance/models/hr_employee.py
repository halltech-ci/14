# -*- coding: utf-8 -*-

from odoo import models, fields, api    

class HrPointage(models.AbstractModel):
    _inherit = "hr.employee.base"
    
    overtime_ids = fields.One2many('hr.attendance', 'employee_id', help='list of attendances for the employee')
    resource_calendar_ids = fields.One2many('resource.calendar')
    resource_calendar_attendance_ids=fiels.One2many(related='resource_calendar_ids.attendance_ids')
    overtime_hours = model.Float(string='overtime', compute='_compute_overtime')
    late = model.Float(string='Late employee', compute='_compute_late')
    
    
    @api.depends('overtime_ids.work_hours','resource_calendar_ids.hours_per_day')
    def _compute_overtime(self):
        overtime = 0
        for employee in self:
            attendances = self.env['hr.attendance'].search([('employee_id', '=', employee.id)])
            for attendance in attendances
                if attendance.work_hours > attendance.resource_calendar_id.hours_per_day: 
                    overtime +=  (attendance.work_hours - attendance.resource_calendar_id.hours_per_day)
            self.overtime_hours = overtime
    
    
    
    @api.depends('overtime_ids.check_in', 'resource_calendar_ids.hours_per_day')
    def _compute_late(self):
        pench_in = resource_calendar_ids.hours_per_day
        for employee in self:
            # start of day in the employee's timezone might be the previous day in utc
            attendances = self.env['hr.attendance'].search([
                ('employee_id', '=', employee.id)])
            
            for attendance in attendances:
                #check_in_days = attendance.check_in.strftime('%A')
                check_in_hour = attendance.check_in.hour
                if check_in_hour > now:
                    check_in = check_in_hour - now
            
            self.late = check_in

