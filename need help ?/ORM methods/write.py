"""
write()
-->The write() method is used to update the records inside the model with the provided values.
 This method accepts a set of dictionary values and the record is updated with these values.

Syntax: Model.write(vals) ? updated record

Eg: self.write({'email': 'demo@cybrosys.info'})

"""

def write(self, values):
	record_ids = self.env['your.model'].search([('name', '=', 'Example')])
	for record in record_ids:
	    record.write({
	        'some_field': 'some_description'
	    })
	return super(ResPartner, self).write(values)