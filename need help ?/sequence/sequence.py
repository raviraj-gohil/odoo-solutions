	sequence_number = fields.Char(string='Sequence Number', readonly=True, index=True)

	@api.model
	def create(self, vals):
	    vals['sequence_number'] = self.env['ir.sequence'].next_by_code('estate_pro_sequence')
	    res = super(EstateProperty, self).create(vals)
	    return res

