garden = fields.Boolean()
garden_area = fields.Integer()
garden_orientation = fields.Selection(selection = [('n','North'), ('s','South'), ('e','East'), ('w','West')])


@api.onchange("garden")
def _onchange_garden(self):
	for rec in self:
		if rec.garden == True:
			rec.garden_area = 10
			rec.garden_orientation = 'n'
		else:
			rec.garden_area = ""
			rec.garden_orientation = ""