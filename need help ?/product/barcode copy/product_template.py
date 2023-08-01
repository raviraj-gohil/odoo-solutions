from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    qrcode = fields.Char('QRcode', compute='_compute_qrcode', inverse='_set_qrcode', search='_search_qrcode')


    @api.depends('product_variant_ids.qrcode')
    def _compute_qrcode(self):
        self.qrcode = False
        for template in self:
            # TODO master: update product_variant_count depends and use it instead
            variant_count = len(template.product_variant_ids)
            if variant_count == 1:
                template.qrcode = template.product_variant_ids.qrcode
            elif variant_count == 0:
                archived_variants = template.with_context(active_test=False).product_variant_ids
                if len(archived_variants) == 1:
                    template.qrcode = archived_variants.qrcode


    def _search_qrcode(self, operator, value):
        query = self.with_context(active_test=False)._search([('product_variant_ids.qrcode', operator, value)])
        return [('id', 'in', query)]


    def _set_qrcode(self):
        variant_count = len(self.product_variant_ids)
        if variant_count == 1:
            self.product_variant_ids.qrcode = self.qrcode
        elif variant_count == 0:
            archived_variants = self.with_context(active_test=False).product_variant_ids
            if len(archived_variants) == 1:
                archived_variants.qrcode = self.qrcode


    def _get_related_fields_variant_template(self):
        # always use super method
        res = super(ProductTemplate, self)._get_related_fields_variant_template()
        res.append('qrcode')
        return res