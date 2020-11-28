# -*- coding: utf-8 -*-
# from odoo import http


# class StockRequest(http.Controller):
#     @http.route('/stock_request/stock_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_request/stock_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_request.listing', {
#             'root': '/stock_request/stock_request',
#             'objects': http.request.env['stock_request.stock_request'].search([]),
#         })

#     @http.route('/stock_request/stock_request/objects/<model("stock_request.stock_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_request.object', {
#             'object': obj
#         })
