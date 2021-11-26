from odoo import models, fields, api, _


class Suspensions(models.Model):
    _name = 'rh.suspensions'
    _description = 'Suspensions'

    name = fields.Char(string='Nombre: ', default="Vacaciones")
    personal_name = fields.Many2one(
        'rh.personal', string='Colaborador', required=True)
    start_date = fields.Date(string='Fecha de inicio: ', required=True)
    end_date = fields.Date(string='Fecha de finalizacion: ', required=True)
    suspensions_days = fields.Integer(string='Dias de suspension: ')
    enjoy_salaries = fields.Boolean(
        string='¿Disfrute de suelo?', default=False)
    suspensions_comment = fields.Text(string='Comentario: ')
