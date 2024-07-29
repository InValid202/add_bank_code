# -*- coding: utf-8 -*-
{
    'name': "CTP Bank Thailand",

    'summary': 'Custom Odoo module introduces Thai bank records, including fields for bank code and bank logo.',

    'description': """
This custom Odoo module enhances the financial management capabilities of Odoo by adding support for Thai bank records. Key features include:

1. **Bank Code Field**: A unique integer field for each bank, formatted to display as a 3-digit number with leading zeros. If the input is less than 3 digits, it will be padded with leading zeros (e.g., 2 will be displayed as 002).

2. **Bank Logo Field**: An image field for storing and displaying the bank's logo. This helps in easily identifying the bank within the system.

These additions streamline the process of managing Thai bank information, providing a more organized and visually identifiable bank record management system.
    """,

    'author': "Cybernetics+",
    'website': "https://www.cybernetics.plus",
    "live_test_url": "https://www.cybernetics.plus",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '17.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],
    "installable": True,
    "application": False,
    "auto_install": False,
    "contributors": [
        "C+ Developer <dev@cybernetics.plus>",
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        "data/bank_data.xml",
    ],
}

