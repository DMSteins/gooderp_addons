# -*- coding: utf-8 -*-
{
    'name': "GOODERP HR模块",
    'author': "开阖软件",
    'website': "http://www.osbzr.com",
    'category': 'gooderp',
    "description": """
    """,
    'version': '8.0.0.1',
    'depends': ['base', 'province_city_county', 'mail'],
    'demo': [
             'tests/staff_demo.xml'
        ],
    'data': [
             'security/ir.model.access.csv',
             'staff.xml',
             'mail_data.xml',
        ],
}
