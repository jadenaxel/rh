{
    'name': 'Recursos Humano',
    'version': '1.0.0',
    'summary': 'Recursos Humanos',
    'description': 'Recursos Humanos',
    'category': 'Human Resources',
    'author': 'Yonderi Diaz Rivera',
    'website': 'https://www.pasp.gob.do',
    'license': 'AGPL-3',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/personal.xml',
        'views/position.xml',
        'views/department.xml',
        'views/formation.xml',
        'views/secure.xml',
        'views/interviews.xml',
        'views/vacancies.xml',
        'views/licenses.xml',
        'views/vacation.xml',
        'views/suspensions.xml',
        'views/admonishments.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
