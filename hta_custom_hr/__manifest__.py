# -*- coding: utf-8 -*-
{
    'name': "hta_custom_hr",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_holidays',
               'hr_payroll',
               'account',
               'hr_payroll_account',
               'project',
               #'hr_timesheet_sheet',
               ],


    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/hr_payslip_views.xml',
        #report
        'reports/report_payslip_book.xml',
        'reports/report_hta_payslip_template.xml',
        'reports/bulletin_paye_report.xml',
        'reports/payslip_reporting_template.xml',
        #wizards
        'wizards/payslip_reporting_book.xml',
        'views/hr_contract_views.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
