# -*- coding: utf-8 -*-
# from odoo import http


# class MartinsamModule(http.Controller):
#     @http.route('/martinsam_module/martinsam_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/martinsam_module/martinsam_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('martinsam_module.listing', {
#             'root': '/martinsam_module/martinsam_module',
#             'objects': http.request.env['martinsam_module.martinsam_module'].search([]),
#         })

#     @http.route('/martinsam_module/martinsam_module/objects/<model("martinsam_module.martinsam_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('martinsam_module.object', {
#             'object': obj
#         })
