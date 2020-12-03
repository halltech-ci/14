# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectEquipementRequest(http.Controller):
#     @http.route('/project_equipement_request/project_equipement_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_equipement_request/project_equipement_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_equipement_request.listing', {
#             'root': '/project_equipement_request/project_equipement_request',
#             'objects': http.request.env['project_equipement_request.project_equipement_request'].search([]),
#         })

#     @http.route('/project_equipement_request/project_equipement_request/objects/<model("project_equipement_request.project_equipement_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_equipement_request.object', {
#             'object': obj
#         })
