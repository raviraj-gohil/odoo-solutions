from odoo import fields, models, api
from datetime import date, timedelta

class CrmLead(models.Model):
    _inherit = "crm.lead"


    def action_snooze14(self):
        self.ensure_one()
        today = date.today()
        my_next_activity = self.activity_ids.filtered(lambda activity: activity.user_id == self.env.user)[:1]
        if my_next_activity:
            if my_next_activity.date_deadline < today:
                date_deadline = today + timedelta(days=14)
            else:
                date_deadline = my_next_activity.date_deadline + timedelta(days=14)
            my_next_activity.write({
                'date_deadline': date_deadline
            })
        return True


    def action_snooze28(self):
        self.ensure_one()
        today = date.today()
        my_next_activity = self.activity_ids.filtered(lambda activity: activity.user_id == self.env.user)[:1]
        if my_next_activity:
            if my_next_activity.date_deadline < today:
                date_deadline = today + timedelta(days=28)
            else:
                date_deadline = my_next_activity.date_deadline + timedelta(days=28)
            my_next_activity.write({
                'date_deadline': date_deadline
            })
        return True
