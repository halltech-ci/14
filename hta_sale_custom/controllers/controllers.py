# -*- coding: utf-8 -*-
# from odoo import http


# class HtaSaleCustom(http.Controller):
#     @http.route('/hta_sale_custom/hta_sale_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_sale_custom/hta_sale_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_sale_custom.listing', {
#             'root': '/hta_sale_custom/hta_sale_custom',
#             'objects': http.request.env['hta_sale_custom.hta_sale_custom'].search([]),
#         })

#     @http.route('/hta_sale_custom/hta_sale_custom/objects/<model("hta_sale_custom.hta_sale_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_sale_custom.object', {
#             'object': obj
#         })
