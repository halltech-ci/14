# -*- coding: utf-8 -*-
# from odoo import http


# class ProductAttribute(http.Controller):
#     @http.route('/product_attribute/product_attribute/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_attribute/product_attribute/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_attribute.listing', {
#             'root': '/product_attribute/product_attribute',
#             'objects': http.request.env['product_attribute.product_attribute'].search([]),
#         })

#     @http.route('/product_attribute/product_attribute/objects/<model("product_attribute.product_attribute"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_attribute.object', {
#             'object': obj
#         })
