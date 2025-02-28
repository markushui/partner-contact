# Copyright 2013-2022 Therp BV <http://therp.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Partner Relations",
    "version": "16.0.1.2.0",
    "author": "Therp BV,Camptocamp,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/partner-contact",
    "complexity": "normal",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "depends": ["contacts", "sales_team"],
    "demo": ["data/demo.xml"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_relation_all.xml",
        "views/res_partner.xml",
        "views/res_partner_relation_type.xml",
        "views/ir_actions_act_window.xml",
        "views/ir_ui_menu.xml",
    ],
    "auto_install": False,
    "installable": True,
}
