from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    property_ids = fields.One2many('estate.property', 'buyer_id')
    prop_count = fields.Integer(compute='_compute_count_number')



    def find_property(self):
        properties = self.property_ids
        return {
        'type':'ir.actions.act_window',
        'name':'Properties',
        'view_mode':'tree',
        'res_model':'estate.property',
        'domain': [('id','in',properties.ids)],
        }


    @api.depends("property_ids")
    def _compute_count_number(self):
        for rec in self:
            count_prop = 0
            for count in rec.property_ids:
                count_prop += 1
            rec.prop_count = count_prop
