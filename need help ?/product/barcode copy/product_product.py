from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'


    qrcode = fields.Char(
        'QRcode', copy=False, index='btree_not_null',
        help="International Article Number used for product identification.")
