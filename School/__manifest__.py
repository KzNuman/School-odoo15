# {
#     'name': 'Hospital Management',
#     'version': '15.0.1.0.0',
#     'category': 'Extra Tools',
#     'summary': 'Module for managing the Hospitals',
#     'sequence': '10',
#     'author': 'Kz Numan, Odoo BD',
#     'maintainer': 'Kz Numan',
#     'website': 'odoomates.com',
#     'depends': [],
#     'demo': [],
#     'data': [
#
#     ],
#     'installable': True,
#     'application': True,
#     'auto_install': False,
# }

{
    'name': "School",

    'summary': """
    School
    
    """,

    'description': """
    School
    """,

    'author': "Numan",
    # 'version': '15.0',

    #any modules necessary for this one to work correctly

    'depends': [],

    #always loaded

    'data': [
        # security
        "security/ir.model.access.csv",

        #views
        "views/student.xml",

        #Teacher
        "views/teacher.xml",

        #Section
        "views/section.xml",

        #Course
        "views/course.xml",

        #Registration
        "views/registration.xml",

        #menu
        "views/menu.xml",


    ],

    #only loaded in demonstration mods

    "Installable": True,
    "application": True,
    "auto_install": False,

}