from odoo import api, fields, models

class CalonAnggota(models.Model):
    _name = "koperasi.calon.anggota"
    _description = "Calon Anggota Koperasi"

    name = fields.Char("Nama Lengkap")
    tanggal_lahir = fields.Date("Tanggal Lahir")
