# -*- coding: utf-8 -*-
# from odoo import http


# class HrOvertimeAutomatic(http.Controller):
#     @http.route('/hr_overtime_automatic/hr_overtime_automatic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_overtime_automatic/hr_overtime_automatic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_overtime_automatic.listing', {
#             'root': '/hr_overtime_automatic/hr_overtime_automatic',
#             'objects': http.request.env['hr_overtime_automatic.hr_overtime_automatic'].search([]),
#         })

#     @http.route('/hr_overtime_automatic/hr_overtime_automatic/objects/<model("hr_overtime_automatic.hr_overtime_automatic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_overtime_automatic.object', {
#             'object': obj
#         })
