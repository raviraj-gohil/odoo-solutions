from odoo import fields, models, api

class SaleOrderAnalytic(models.Model):
    _inherit = 'sale.order.line'


    analytic_id = fields.Many2one('account.analytic.account')


    @api.onchange('analytic_id')
    def _onchange_analytic(self):
        for rec in self:
            print('----------------------------------------------------------work')
            rec.analytic_id = rec.order_id.analytic_account_id
            # print('----------------------------------------------------------', rec.analytic_account_id)