# -*- coding: utf-8 -*-

from openerp import api, fields, models

import logging
logger = logging.getLogger(__name__)


class ResPartnerNamePlaque(models.Model):
    _inherit = 'res.partner'

    name_plaque_line1 = fields.Char(string='Name Plaque Line 1', size=15)
    name_plaque_line2 = fields.Char(string='Name Plaque Line 2', size=15)

    def create_plaque_mail_message(self, partner, values):
        if "name_plaque_line1" in values or "name_plaque_line2" in values:
            line1 = values.get('name_plaque_line1', '')
            line2 = values.get('name_plaque_line2', '')
            message_body = line1 + "\n" + \
                           line2 + "\n" + \
                           '---\n' +\
                           'Namensplakette'

            logger.debug("Found name plaque fields (\"%s\", \"%s\"). Creating mail.message"
                         % (line1, line2))

            partner.sudo().with_context(mail_post_autofollow=False).message_post(
                body=message_body,
                type='comment',
                subtype='fso_mail_message_subtypes_name_plaque.fson_name_plaque',
                content_subtype="plaintext")

    @api.model
    def create(self, values):
        partner = super(ResPartnerNamePlaque, self).create(values)
        self.create_plaque_mail_message(partner, values)
        return partner

    @api.multi
    def write(self, values):
        res = super(ResPartnerNamePlaque, self).write(values)

        for p in self:
            self.create_plaque_mail_message(p, values)

        return res
