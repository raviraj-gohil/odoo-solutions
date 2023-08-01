from odoo import fields, models, api

class SaleOrderAnalytic(models.Model):
    _inherit = 'crm.lead'


    pricelist_id = fields.Many2one(comodel_name='product.pricelist', string="Pricelist")   
    payment_term_id = fields.Many2one(comodel_name='account.payment.term', string="Payment Terms") 

-----------------------------------------------------------------------------------------------

from odoo import fields, models, api

class ZoroSaleOrder(models.Model):
    _inherit = 'sale.order'


    @api.onchange('tag_ids')
    def set_value(self):
        crm_id = self.env['crm.lead'].browse(self.env.context.get('active_id'))
        print('---------------------------------------',crm_id)
        self.pricelist_id = crm_id.pricelist_id
        self.payment_term_id = crm_id.payment_term_id