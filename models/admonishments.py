from odoo import models, fields, api, _


class Admonishments(models.Model):
    _name = 'rh.admonishments'
    _description = 'Admonishments'

    name = fields.Char(string='Nombre: ', default="Amonestaciones")
    personal_name = fields.Many2one(
        'rh.personal', string='Colaborador', required=True)
    start_date = fields.Date(string='Fecha: ', required=True)
    enjoy_salaries = fields.Boolean(
        string='¿El colaborador puede disfrutar de los salarios?', default=False)
    category = fields.Selection(
        [('verbal', 'Verbal'), ('escrita', 'Escrita'), ('tercer', 'Tercer grado')], string="Amonestaciones")
    admonishments_comment = fields.Text(string='Comentario: ')
