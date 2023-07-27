from odoo import models, fields, api

class EstateWizard(models.TransientModel):
   _name = 'estate.wizard'
   _description = 'Session Wizard'

   old_salesman = fields.Many2one("res.users", string="Old SalesMan")
   new_salesman = fields.Many2one("res.users", string="New SalesMan")
   salesman_id = fields.Many2one("res.users", string="SalesMan")

# for update whole module

   # def add_info(self):
   #    properties = self.env['estate.property'].search([('salesman_id', '=', self.old_salesman.id)])
   #    properties.salesman_id = self.new_salesman


# for single record

   def add_info(self):
      property_id = self.env['estate.property'].browse(self.env.context.get('active_id'))
      property_id.salesman_id = self.salesman_id


# property_id = self.env['estate.property'].browse(self.env.context.get('active_id'))