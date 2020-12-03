# -*- coding: utf-8 -*-
# from odoo import http


# class HtaMrp(http.Controller):
#     @http.route('/hta_mrp/hta_mrp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_mrp/hta_mrp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_mrp.listing', {
#             'root': '/hta_mrp/hta_mrp',
#             'objects': http.request.env['hta_mrp.hta_mrp'].search([]),
#         })

#     @http.route('/hta_mrp/hta_mrp/objects/<model("hta_mrp.hta_mrp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_mrp.object', {
#             'object': obj
#         })
