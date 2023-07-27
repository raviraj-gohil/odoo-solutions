current_date = fields.Date(default=fields.date.today())
validity = fields.Integer(default=7)
date_deadline = fields.Date(compute='_compute_date_deadline',inverse='_inverse_date_deadline')



@api.depends("validity")
def _compute_date_deadline(self):
	for record in self:
			record.date_deadline = False
			if record.validity:
				record.date_deadline = record.current_date + timedelta(days=record.validity)

@api.depends('date_deadline')
def _inverse_date_deadline(self):
	for record in self:
		if record.date_deadline:
			record.validity = (record.date_deadline - record.current_date).days