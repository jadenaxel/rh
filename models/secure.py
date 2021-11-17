from odoo import models, fields, api, _


class Secure(models.Model):
    _name = 'rh.secure'
    _description = 'Secure'

    name = fields.Char(string='Tipo de seguro', required=True)
