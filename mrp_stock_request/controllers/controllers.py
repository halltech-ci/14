# -*- coding: utf-8 -*-
# from odoo import http


# class MrpStockRequest(http.Controller):
#     @http.route('/mrp_stock_request/mrp_stock_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_stock_request/mrp_stock_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_stock_request.listing', {
#             'root': '/mrp_stock_request/mrp_stock_request',
#             'objects': http.request.env['mrp_stock_request.mrp_stock_request'].search([]),
#         })

#     @http.route('/mrp_stock_request/mrp_stock_request/objects/<model("mrp_stock_request.mrp_stock_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_stock_request.object', {
#             'object': obj
#         })
