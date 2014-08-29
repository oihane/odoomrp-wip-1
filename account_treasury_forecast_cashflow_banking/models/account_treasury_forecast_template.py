# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from openerp import models, fields


class AccountTreasuryForecastReceivableemplate(models.Model):
    _inherit = 'account.treasury.forecast.receivable.template'

    payment_mode_id = fields.Many2one("payment.mode", string="Payment Mode")


class AccountTreasuryForecastCashflowTemplate(models.Model):
    _inherit = 'account.treasury.forecast.cashflow.template'

    payment_mode_id = fields.Many2one("payment.mode", string="Payment Mode")
