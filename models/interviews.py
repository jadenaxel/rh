from odoo import models, fields, api, _


class Interview(models.Model):
    _name = 'rh.interview'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Interviews'

    name = fields.Char(string='Nombre: ', required=True)
    cedula = fields.Char(string='Cédula: ', required=True)
    vacancies_type = fields.Many2one(
        'rh.vacancies', string='Vacante: ', required=True)
    resume_date = fields.Date(string='Fecha de entrega de curriculum: ')
    pre_interview = fields.Datetime(string='Fecha de pre entrevista: ')
    interview = fields.Datetime(string='Fecha de entrevista: ')
    
    state = fields.Selection([('draft', 'Borrador'), ('confirm', 'Confirmado'), (
        'done', 'Completado'), ('cancel', 'Cancelado')], default='draft', string='Estado', tracking=True)

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'
