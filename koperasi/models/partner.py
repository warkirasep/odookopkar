from odoo import api, fields, models

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    is_member = fields.Boolean("Is Member Koperasi", default=True)
    is_active = fields.Boolean("Is Aktif", default=True)
