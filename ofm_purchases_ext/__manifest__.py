# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Trinity Roots :: OFM - Module Purchases Extend",
    "summary": "Module summary",
    "version": "8.0.1.0.0",
    "category": "Uncategorized",
    "description": """

add another field & method to purchases for ofm

    """,
    "website": "http://www.trinityroots.co.th/",
    "author": "Trinity Roots",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        'purchase',
        'pos_customize',
        'tr_core_update',
    ],
    "data": [
        'data/data.xml',
        'security/ir.model.access.csv',
        'wizards/received_product_report_view.xml',
        'wizards/po_report_view.xml',
        'wizards/pr_report_view.xml',
        'wizards/po_ship_date_report_view.xml',
        'wizards/detail_product_report_view.xml',
        'wizards/po_amount_report_view.xml',
    ],
    "demo": [],
    "qweb": []
}
