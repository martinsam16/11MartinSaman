# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Persona(models.Model):
    _name = 'martinsam_module.persona'
    _description = 'Persona model'

    nombres = fields.Char(string='Nombres persona')
    apellidos = fields.Char(string='Apellidos de la persona')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
