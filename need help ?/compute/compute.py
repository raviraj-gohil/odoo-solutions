total_area = fields.Integer(compute='_compute_total_area')
living_area = fields.Integer(string="Living Area (sqm)")
garden_area = fields.Integer()


@api.depends('living_area','garden_area')
def _compute_total_area(self):
	for area in self:
		area.total_area = area.living_area + area.garden_area