from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    employee_id = fields.Char('Employee ID')
    login_count = fields.Integer("Number of logins", compute="_compute_login_count")

    _sql_constraints = [('employee_id', 'unique(employee_id)', 'Employee ID must be unique!')]

    def _compute_login_count(self):
        user = self
        self.env.cr.execute("""
            SELECT count(*)
              FROM res_users_log
             WHERE create_uid=%s
        """ % (user.id))
        user.login_count = self.env.cr.dictfetchall()[0].get('count')
