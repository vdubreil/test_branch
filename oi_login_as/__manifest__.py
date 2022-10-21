# -*- coding: utf-8 -*-
{
'name': 'Login as another user',
'summary': 'Login as/impersonate another user, Login As, Other Users, Admin Users, '
           'Administrator, Super User, Portal User, Portal Hijack',
'version': '13.0.1.1.10',
'category': 'Extra Tools',
'website': 'https://www.open-inside.com',
'description': '''
'''
               '''		 * allow administrator to login as/impersonate normal user
'''
               '''		 * allow administrator to login as/impersonate portal user
'''
               '''		 * login back to administrator
'''
               '''		 
'''
               '    ',
'images': ['static/description/cover.png'],
'author': 'Openinside',
'license': 'OPL-1',
'price': 30.0,
'currency': 'USD',
'installable': True,
'depends': ['web'],
'data': ['view/login_as.xml', 'view/action.xml', 'view/web_assets.xml'],
'qweb': ['static/src/xml/templates.xml'],
'external_dependencies': {},
'auto_install': True,
'odoo-apps': True,
'application': False
}