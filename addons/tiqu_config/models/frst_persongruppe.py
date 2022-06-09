# -*- coding: utf-8 -*-

from openerp import models, fields, api

import logging

logger = logging.getLogger(__name__)


# PersonEmailGruppe: FRST groups for email addresses
class FRSTPersonGruppeWitaConfig(models.Model):
    _inherit = "frst.persongruppe"

    _checkbox_fields_group_identifier = {
        'donation_deduction_optout_web': 110493,
        'donation_deduction_disabled': 128782,
        'donation_receipt_web': 20168,
        'opt_out': 11102,
        'sponsor_report_email': 406001,
        'sponsor_report_post': 406002,
    }
    logger.info("TIQU frst.persongruppe _checkbox_fields_group_identifier: %s" % _checkbox_fields_group_identifier)