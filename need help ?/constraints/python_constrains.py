@api.constrains('selling_price')
def _check_profit(self):
	for rec in self:
		# if float_compare(rec.selling_price) < (rec.expected_price * 90) / 100:
		for x in rec.offer_ids:
			if x.status != "accepted" and rec.selling_price != 0:
				if rec.selling_price < (rec.expected_price * 90) / 100:
					raise ValidationError("offer lower than 90% of the expected price.")