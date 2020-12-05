# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectStock(http.Controller):
#     @http.route('/project_stock/project_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_stock/project_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_stock.listing', {
#             'root': '/project_stock/project_stock',
#             'objects': http.request.env['project_stock.project_stock'].search([]),
#         })

#     @http.route('/project_stock/project_stock/objects/<model("project_stock.project_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_stock.object', {
#             'object': obj
#         })
