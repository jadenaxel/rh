from odoo import models, fields, api, _


class Vacancy(models.Model):
    _name = 'rh.vacancies'
    _description = 'Vacancy'

    name = fields.Char(string='Nombre de la vacante: ', required=True)
