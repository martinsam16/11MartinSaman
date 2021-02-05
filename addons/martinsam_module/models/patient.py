# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    birthdate = fields.Date(string='Birthdate')
    age = fields.Integer(string='Age', compute='_compute_age')  # store=True
    is_adult = fields.Boolean(string='Adult')
    number_consults = fields.Integer(string='Number of consults', readonly=True)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Patient contact')
    mobile = fields.Char(string='Mobile', related='partner_id.mobile')

    @api.depends('birthdate')
    def _compute_age(self):
        for rec in self:
            age = 0
            if rec.birthdate:
                age = fields.Date.today().year - rec.birthdate.year
            rec.age = age

    # como una ayuda, el campo es editable.
    # Se ejecuta por acciones de interfaz
    # Se guarda en la db
    @api.onchange('birthdate')
    def _onchange_birthdate(self):
        for rec in self:
            is_adult = False
            age = 0
            if rec.birthdate:
                age = fields.Date.today().year - rec.birthdate.year
            if age >= 18:
                is_adult = True
            rec.age = age
            rec.is_adult = is_adult

    @api.constrains('birthdate')
    def _check_birthdate(self):
        for rec in self:
            if rec.birthdate > fields.Date.today():
                raise ValidationError('Birthdate cannot be older than current date')

    def consult_finish(self):
        for rec in self:
            rec.number_consults += 1
