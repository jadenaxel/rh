from odoo import models, fields, api, _


class Department(models.Model):
    _name = 'rh.department'
    _description = 'Department'

    name = fields.Char(string='Departamento', required=True, tracking=True)
