# -*- coding: utf-8 -*-

{
    'name': 'Print Journal Entries Report',
    'version': '13.0.0.0',
    'category': 'Account',
    'summary': 'Print Journal Entries with its journal item as PDF.',
    'description': """
        Print journal entry with its journal item as pdf 
        """,
    'author': 'Ahmed Elsayed Aldamhogy ',
    'depends': ['base', 'account'],
    'data': [
        'report/report_journal_entries.xml',
        'report/report_journal_entries_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
