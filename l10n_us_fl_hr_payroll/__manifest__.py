# -*- encoding: utf-8 -*-
{
    'name': 'USA - Florida - Payroll',
    'author': 'Hibou Corp. <hello@hibou.io>',
    'license': 'AGPL-3',
    'category': 'Localization',
    'depends': ['l10n_us_hr_payroll'],
    'version': '11.0.2019.0.0',
    'description': """
USA::Florida Payroll Rules.
===========================

    * Florida Department of Revenue partner
    * Contribution register for Florida DoR
    * Company level Florida Unemployment Rate
    """,

    'auto_install': False,
    'website': 'https://hibou.io/',
    'data':[
        'us_fl_hr_payroll_view.xml',
        'data/base.xml',
        'data/rules_2016.xml',
        'data/rules_2017.xml',
        'data/rules_2018.xml',
        'data/rules_2019.xml',
        'data/final.xml',
    ],
    'installable': True
}
