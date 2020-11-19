# -*- coding: utf-8 -*-
# from odoo import http


# class HtaCustomAttendance(http.Controller):
#     @http.route('/hta_custom_attendance/hta_custom_attendance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_custom_attendance/hta_custom_attendance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_custom_attendance.listing', {
#             'root': '/hta_custom_attendance/hta_custom_attendance',
#             'objects': http.request.env['hta_custom_attendance.hta_custom_attendance'].search([]),
#         })

#     @http.route('/hta_custom_attendance/hta_custom_attendance/objects/<model("hta_custom_attendance.hta_custom_attendance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_custom_attendance.object', {
#             'object': obj
#         })
