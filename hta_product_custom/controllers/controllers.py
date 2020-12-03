# -*- coding: utf-8 -*-
# from odoo import http


# class HtaProductCustom(http.Controller):
#     @http.route('/hta_product_custom/hta_product_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_product_custom/hta_product_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_product_custom.listing', {
#             'root': '/hta_product_custom/hta_product_custom',
#             'objects': http.request.env['hta_product_custom.hta_product_custom'].search([]),
#         })

#     @http.route('/hta_product_custom/hta_product_custom/objects/<model("hta_product_custom.hta_product_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_product_custom.object', {
#             'object': obj
#         })
