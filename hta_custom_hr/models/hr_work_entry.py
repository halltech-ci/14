# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class hta_custom_hr(models.Model):
#     _name = 'hta_custom_hr.hta_custom_hr'
#     _description = 'hta_custom_hr.hta_custom_hr'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HrWorkEntry(models.Model):
    _inherit = "hr.work.entry.type"
    
    @api.model
    def prepare_overtime_days(self):
        
        res = []
        round_days = 'FULL'
        round_days_type = 'DOWN'
        # Create one worked days record for each timesheet sheet
        res = [{
                'name': 'Overtime',
                'code': 'HS',
                'round_days': round_days,
                'round_days_type':round_days_type,
              }]
        
        worked_days_data = res
        if worked_days_data:
        
            return self.env['hr.work.entry.type'].create(worked_days_data)

