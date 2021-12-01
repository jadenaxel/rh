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
    salary = fields.Float(string='Salario: ', tracking=True)
    net_salary = fields.Float(string='Salario neto: ', tracking=True)
    gross_salary = fields.Float(string='Salario bruto: ', tracking=True)
    cooperative = fields.Boolean(string='Cooperativa: ', tracking=True)
    child_quantity = fields.Integer(
        string='Cantidad de hijos: ', tracking=True)
    mother_name = fields.Char(string='Nombre de la madre: ', tracking=True)
    father_name = fields.Char(string='Nombre del padre: ', tracking=True)
    civil_status = fields.Selection([
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('viudo', 'Viudo')
    ], string='Estado civil: ', tracking=True)
    couple_name = fields.Char(string='Nombre de la pareja: ', tracking=True)
    religion = fields.Selection([
        ('catolico', 'Católico'),
        ('cristiano', 'Cristiano'),
        ('judio', 'Judio'),
        ('musulman', 'Musulman'),
        ('budista', 'Budista'),
        ('hindu', 'Hindu'),
        ('otro', 'Otro')
    ], string='Religión: ', tracking=True)
    ideology = fields.Char(string='Ideología: ', tracking=True)
    address = fields.Char(string='Dirección: ', tracking=True)
    email = fields.Char(string='Correo: ', tracking=True)
    license_quantity = fields.One2many(
        'rh.licence', 'personal_name', string='Licencias: ', tracking=True)
    vacations = fields.One2many(
        'rh.vacation', 'personal_name', string="Vacaciones: ", tracking=True)
    suspensions = fields.One2many(
        'rh.suspensions', 'personal_name', string='Suspensiones: ', tracking=True)
    admonishmets = fields.One2many(
        'rh.admonishments', 'personal_name', string="Amonestaciones")
