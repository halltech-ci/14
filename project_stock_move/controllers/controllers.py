# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectStockMove(http.Controller):
#     @http.route('/project_stock_move/project_stock_move/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_stock_move/project_stock_move/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_stock_move.listing', {
#             'root': '/project_stock_move/project_stock_move',
#             'objects': http.request.env['project_stock_move.project_stock_move'].search([]),
#         })

#     @http.route('/project_stock_move/project_stock_move/objects/<model("project_stock_move.project_stock_move"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_stock_move.object', {
#             'object': obj
#         })
