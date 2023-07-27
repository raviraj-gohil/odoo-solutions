from odoo import models, fields


class EstateSchedule(models.Model):
   _name = 'estate.schedule'


   def action_done(self):
      properties = self.env['estate.property'].search([('status', '=', 'cancel')])
      for pro in properties:
         pro.active = False
