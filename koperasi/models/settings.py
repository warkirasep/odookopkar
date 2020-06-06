from odoo import api, fields, models

class Settings(models.TransientModel):
	_inherit = 'res.config.settings'

	#Simpanan
	max_simp_pokok = fields.Char(string="Maksimal Simpanan Pokok")
	max_simp_wajib = fields.Char(string="Maksimal Simpanan Wajib")
	cost_adm_member_out = fields.Char(string="Biaya Administrasi Keluar Anggota")

	#Pinjaman reguler
	max_pinj_reguler = fields.Char(string="Maksimal Pinjaman Reguler")
	pinj_reguler_pengurus = fields.Char(string="Jasa Pinjaman Reguler Pengurus")
	pinj_reguler_anggota = fields.Char(string="Jasa Pinjaman Reguler Member")

	#Pinjaman Barang
	max_pinj_barang = fields.Char(string="Maksimal Pinjaman Barang")
	pinj_barang_pengurus = fields.Char(string="Jasa Pinjaman Barang Pengurus")
	pinj_barang_anggota = fields.Char(string="Jasa Pinjaman Barang Member")

	#Pinjaman Bank
	max_pinj_bank = fields.Char(string="Maksimal Pinjaman Bank")

	def set_values(self):
		res = super(Settings, self).set_values()
		self.env['ir.config_parameter'].set_param('koperasi.max_simp_pokok', self.max_simp_pokok)
		self.env['ir.config_parameter'].set_param('koperasi.max_simp_wajib', self.max_simp_wajib)
		self.env['ir.config_parameter'].set_param('koperasi.cost_adm_member_out', self.cost_adm_member_out)
		return res

	@api.model
	def get_values(self):
		res = super(Settings, self).get_values()
		ICPSudo = self.env['ir.config_parameter'].sudo()
		max_simp_pokok = ICPSudo.get_param('koperasi.max_simp_pokok')
		max_simp_wajib = ICPSudo.get_param('koperasi.max_simp_wajib')
		cost_adm_member_out = ICPSudo.get_param('koperasi.cost_adm_member_out')
		res.update(
			max_simp_pokok = max_simp_pokok,
			max_simp_wajib = max_simp_wajib,
			cost_adm_member_out = cost_adm_member_out
		)
		return res