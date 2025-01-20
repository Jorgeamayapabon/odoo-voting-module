manifest = {
    'name': "University Voting System",
    'version': "1.0",
    'depends': ['base', 'web'],
    'author': "Jorge Enrique Amaya Pabón",
    'data': [
        'views/university_sedes_view.xml',
        'views/university_voting_process_view.xml',
        'views/university_student_web_template.xml',
        'wizards/voting_import_wizard_view.xml'
    ],
    'installable': True,
    'application': True,
}
