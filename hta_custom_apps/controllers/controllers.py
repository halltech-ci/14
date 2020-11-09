# -*- coding: utf-8 -*-
# from odoo import http


# class HtaCustomApps(http.Controller):
#     @http.route('/hta_custom_apps/hta_custom_apps/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_custom_apps/hta_custom_apps/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_custom_apps.listing', {
#             'root': '/hta_custom_apps/hta_custom_apps',
#             'objects': http.request.env['hta_custom_apps.hta_custom_apps'].search([]),
#         })

#     @http.route('/hta_custom_apps/hta_custom_apps/objects/<model("hta_custom_apps.hta_custom_apps"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_custom_apps.object', {
#             'object': obj
#         })
