# -*- coding: utf-8 -*-
# from odoo import http


# class HtaProjectCustom(http.Controller):
#     @http.route('/hta_project_custom/hta_project_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_project_custom/hta_project_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_project_custom.listing', {
#             'root': '/hta_project_custom/hta_project_custom',
#             'objects': http.request.env['hta_project_custom.hta_project_custom'].search([]),
#         })

#     @http.route('/hta_project_custom/hta_project_custom/objects/<model("hta_project_custom.hta_project_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_project_custom.object', {
#             'object': obj
#         })
