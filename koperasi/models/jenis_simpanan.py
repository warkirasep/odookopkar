from odoo import api, fields, models

class JenisSimpanan(models.Model):
	_name = "koperasi.jenis.simpanan"

	name = fields.Char("Name")
	code = fields.Char("Code")
	description = fields.Text("Description")
	tipe_simpanan = fields.Selection([('sr', 'Simpanan Reguler'), ('sb', 'Simpanan Berjangka'), ('sw', 'Simpanan Wajib')])