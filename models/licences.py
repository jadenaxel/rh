from odoo import models, fields, api, _


class Licence(models.Model):
    _name = 'rh.licence'
    _description = 'Licence'

    name = fields.Char(string='Nombre: ', default="Licencias")
    personal_name = fields.Many2one(
        'rh.personal', string='Colaborador', required=True)
    start_date = fields.Date(string='Fecha de inicio: ', required=True)
    end_date = fields.Date(string='Fecha de finalizacion: ', required=True)
    licence_comment = fields.Text(string='Comentario: ', required=True)
