# -*- coding: utf-8 -*-
{
    'name' : 'Base Magang',
    'version' : '1.1',
    'summary': 'Add menu and fields in res.partner',
    'sequence': 1,
    'author': 'Eka',
    'description': """
        - Create Menu Branch.\n
          Created by : Ibnu \n
        - Create Menu Salesman.\n
          Created by : Vicky \n
        - Add field Branch in res.users.\n
          created by : Hilmy \n
    """,
    'category' : 'Base',
    'website': '',
    'images' : [],
    'depends' : ['base'],
    'data': [
        'views/res_partner_view.xml',
        'views/res_users_view.xml'
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
