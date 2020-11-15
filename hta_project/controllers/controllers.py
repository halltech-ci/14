# -*- coding: utf-8 -*-
# from odoo import http


# class HtaProject(http.Controller):
#     @http.route('/hta_project/hta_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_project/hta_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_project.listing', {
#             'root': '/hta_project/hta_project',
#             'objects': http.request.env['hta_project.hta_project'].search([]),
#         })

#     @http.route('/hta_project/hta_project/objects/<model("hta_project.hta_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_project.object', {
#             'object': obj
#         })
