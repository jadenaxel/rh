from odoo import models, fields, api, _


class Vacation(models.Model):
    _name = 'rh.vacation'
    _description = 'Vacation'

    name = fields.Char(string='Nombre: ', default="Vacaciones")
    personal_name = fields.Many2one(
        'rh.personal', string='Colaborador', required=True)
    start_date = fields.Date(string='Fecha de inicio: ', required=True)
    end_date = fields.Date(string='Fecha de finalizacion: ', required=True)
    enjoy_salaries = fields.Boolean(
        string='¿Disfrute de suelo?', default=False)
    vacation_comment = fields.Text(string='Comentario: ')
