from odoo import models, fields, api, _


class Personal(models.Model):
    _name = 'rh.personal'
    _description = 'Personal'

    name = fields.Char(string='Nombre: ', required=True, tracking=True)
    last_name = fields.Char(string='Apellido: ', required=True, tracking=True)
    gender = fields.Selection([
        ('female', 'Femenino'),
        ('male', 'Masculino')
    ], string="Genero: ", required=True, default='female', tracking=True)
    job_position_name = fields.Many2one(
        'rh.position', string='Cargo: ', required=True)
    deparmtnet_name = fields.Many2one(
        'rh.department', string='Departamento: ', required=True)
    numberPhone = fields.Char(
        string='Telefono: ', required=True, tracking=True)
    secure = fields.Many2one(
        'rh.secure', string="Tipo de Seguro: ", required=True)
    nss_code = fields.Char(string='NSS: ', required=True, tracking=True)
    birth_date = fields.Date(
        string='Fecha de nacimiento: ', required=True, tracking=True)
    emergency_contact = fields.Char(
        string='Contacto de emergencia: ', required=True, tracking=True)
    formation = fields.Many2one(
        'rh.formation', string='Formación: ', required=True)
    portrai_image = fields.Binary(
        string='Foto: ', required=True, tracking=True)
    home_number = fields.Char(
        string='Telefono de casa: ', required=True, tracking=True)
    blood_type = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    ], string='Tipo de sangre: ', required=True, tracking=True)
    number_account = fields.Char(
        string='Numero de cuenta: ', required=True, tracking=True)
    ocupational_status = fields.Selection([
        ('i', 'I'),
        ('ii', 'II'),
        ('iii', 'III'),
        ('iv', 'IV'),
        ('v', 'V'),
    ], string="Grupo occupacional: ", required=True, tracking=True)
    staff_type = fields.Selection([
        ('fijo', 'Empleados Fijos'),
        ('contratado', 'Empleados Contratados'),
        ('militares', 'Militares')
    ], string='Tipos de Empleado: ', required=True, tracking=True)
    income_date = fields.Date(
        string='Fecha de ingreso: ', required=True, tracking=True)
    exit_date = fields.Date(string='Fecha de salida: ', tracking=True)
