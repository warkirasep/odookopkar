from odoo import api, fields, models

class Anggota (models.Model):
    _name = 'koperasi.anggota'
    _description = 'Anggota Koperasi'

    name = fields.Char("Name")
    user_id = fields.Many2many(
                comodel_name="res.users",
                string="User Login Anggota")