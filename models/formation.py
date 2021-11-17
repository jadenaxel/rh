from odoo import models, fields, api, _

class Formation(models.Model):
    _name = 'rh.formation'
    _description = 'Formation'

    name = fields.Char(string='Formacion: ', required=True)
