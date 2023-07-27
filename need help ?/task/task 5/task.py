from odoo import fields, models, api

class ZoroSaleOrder(models.Model):
    _inherit = 'sale.order'

    service_total = fields.Float(compute='_compute_service_total', store=True)

    @api.depends('order_line')
    def _compute_service_total(self):
        for rec in self:
            prices = rec.order_line.filtered(lambda x: x.product_id.detailed_type == 'service')
            rec.service_total = sum(prices.mapped('price_subtotal'))

