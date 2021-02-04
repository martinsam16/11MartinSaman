from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    sunat_serie = fields.Char(string='Sunat serie', size=4)
    sunat_correlative = fields.Char(string='Sunat correlative', size=10)
