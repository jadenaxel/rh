from odoo import models, fields, api, _


class Position(models.Model):
    _name = 'rh.position'
    _description = 'Posición de Trabajo'

    name = fields.Char(string='Posición de Trabajo:',
                       required=True, trackng=True)
