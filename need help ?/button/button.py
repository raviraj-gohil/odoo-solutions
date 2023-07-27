status = fields.Selection(selection = [('new', 'New'),('sold', 'SOLD'), ('cancel', 'Canceled')], default='new')


@api.depends('status')
def sold_property(self):
	for rec in self:
		if rec.status != 'cancel':
			if rec.status == 'accepted':
				rec.status = 'sold'
			else:
				raise UserError('Need to Accept one offer')	
		else:
			raise UserError('A canceled property cannot be set as sold')