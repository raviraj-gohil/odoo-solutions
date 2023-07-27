"""
create()
--> The create() method is used to create new records for the model.
 This method accepts a set of dictionary values and new records are initialized with it

 Syntax: Model.create(vals_list) ? records

 Eg: self.create({'name': 'Cybrosys', 'email': 'demo@cybrosys.com'})
 
"""

@api.model
def create(self,vals):

     vals = {'name': 'ABC', 'standard':10}

     res = super(students, self).create(vals)

     return res