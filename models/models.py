# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re


class AddBankCode(models.Model):

    _inherit = 'res.bank'

    bank_code = fields.Char(string='Bank Code',)
    bank_logo = fields.Binary(string='Bank logo')

    @api.onchange('bank_code')
    def _onchange_bank_code(self):
        if self.bank_code:

            # filter for numeric character
            if not self.bank_code.isdigit():
                temp_bank_code = ""
                for char in self.bank_code:
                    if char.isdigit():
                        temp_bank_code += char
                self.bank_code = temp_bank_code

            # get only first 3 number
            if len(self.bank_code) > 3:
                self.bank_code = self.bank_code[:3]
            else:
                self.bank_code = self.bank_code.zfill(3)
