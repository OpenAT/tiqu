# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'fso_partner_name_plaque',
    'summary': """Adds two name plaque fields to partner.""",
    'description': """
Adds two name plaque fields to partner.
    """,
    'author': 'DataDialog',
    'version': '0.1',
    'website': 'https://www.datadialog.net',
    'installable': True,
    'depends': [
        'fso_mail_message_subtypes_name_plaque',
    ],
    'data': [
        'views/templates.xml',
    ],
}