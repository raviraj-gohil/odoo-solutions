offer_ids = fields.One2many("estate.property.offer", "property_id")
best_price = fields.Float(compute='_compute_highest_price')


@api.depends("offer_ids")
def _compute_highest_price(self):
	self.best_price = max(self.offer_ids.mapped('price'),default=0)