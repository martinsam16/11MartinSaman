# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'

    name = fields.Char(string='Name patient', required=True)
    surname = fields.Char(string='Surname', required=True)
    birthdate = fields.Date(string='Birthdate')
