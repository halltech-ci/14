# -*- coding: utf-8 -*-
# from odoo import http


# class Infoemploye(http.Controller):
#     @http.route('/infoemploye/infoemploye/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infoemploye/infoemploye/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('infoemploye.listing', {
#             'root': '/infoemploye/infoemploye',
#             'objects': http.request.env['infoemploye.infoemploye'].search([]),
#         })

#     @http.route('/infoemploye/infoemploye/objects/<model("infoemploye.infoemploye"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infoemploye.object', {
#             'object': obj
#         })
