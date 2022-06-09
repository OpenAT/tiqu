# -*- coding: utf-8 -*-

from openerp import models, fields, api

import logging
_logger = logging.getLogger(__name__)


# Additional fields for the web checkout
class ResPartnerWitaConfig(models.Model):
    _inherit = 'res.partner'

    sponsor_report_email = fields.Boolean(string="Sponsor report via E-Mail")
    sponsor_report_post = fields.Boolean(string="Sponsor report via postal service")
