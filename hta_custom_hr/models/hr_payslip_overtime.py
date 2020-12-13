# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import datetime

class HrPayslip(models.Model):
    _inherit = "hr.payslip"
    
    @api.model
    def prepare_overtime_days(self, employee, overtime, payslip, date_from, date_to):
        
        domaine = [
            ('name', '=', 'Overtime'),
        ]
        
        overtimes = self.env['bt.hr.overtime'].search([])
        
        work_entry_type = self.env['hr.work.entry.type'].search(domaine)
        number_of_hours = 0
        number_of_days = 0
        for overtime in overtimes:
            t = overtime.start_date
            date = t.date()
            if date_from <= date <= date_to:
                number_of_hours += overtime.overtime_hours
                number_of_days += (overtime.overtime_hours / 8)
      
        # Get formated date from the timesheet sheet
        #date_from_formated = overtimes.start_date
                    
        if number_of_hours > 0 or number_of_days > 0:

            return{
                'name': _('Overtime'),
                'sequence': work_entry_type.sequence,
                'work_entry_type_id': work_entry_type.id,
                'number_of_hours': number_of_hours,
                'number_of_days':number_of_days,
                'contract_id': payslip.contract_id.id,
                'imported_from_overtime': True,
                'payslip_id': payslip.id,
            }
        return False


    def _overtime_mapping(self, overtimes, payslip, date_from, date_to):
        """This function takes timesheet objects imported from the timesheet
        module and creates a dict of worked days to be created in the payslip.
        """
        # Create one worked days record for each timesheet sheet
        for overtime in overtimes:
            worked_days_data = self.prepare_overtime_days(
                payslip.employee_id, overtime, payslip,date_from, date_to)
        if worked_days_data:
            self.env['hr.payslip.worked_days'].create(worked_days_data)



    def _check_contract(self):
        """Contract is not required field for payslips, yet it is for
        payslips.worked_days."""
        for payslip in self:
            if not payslip.contract_id:
                raise UserError(
                    _("Contract is not defined for one or more payslips."),
                )
                
    @api.model
    def get_overtimes_from_employee(self, employee, date_from, date_to):
        criteria = [
            ('start_date', '>=', date_from),
            ('start_date', '<=', date_to),
            ('state', '=', 'validate'),
            ('employee_id', '=', employee.id),
        ]
        overtime_model = self.env['bt.hr.overtime']
        overtimes = overtime_model.search(criteria)
        if not overtimes:
            raise UserError(
                _("Sorry, but there is no approved Overtimes for the \
                entire Payslip period for user %s") % employee.name,
            )
        return overtimes
    
    

    def import_overtime_days(self):
        """This method retreives the employee's Overtimes for a payslip period
        and creates worked days records from the imported timesheets
        """
        self._check_contract()
        for payslip in self:
            date_from = payslip.date_from
            date_to = payslip.date_to

            # Delete old imported worked_days
            # The reason to delete these records is that the user may make
            # corrections to his timesheets and then reimport these.
            self.env['hr.payslip.worked_days'].search(
                [('payslip_id', '=', payslip.id),
                 ('imported_from_overtime', '=', True)]).unlink()

            # get timesheet sheets of employee
            overtimes = self.get_overtimes_from_employee(
                payslip.employee_id, date_from, date_to)
            # The reason to call this method is for other modules to modify it.
            self._overtime_mapping(overtimes, payslip, date_from, date_to)