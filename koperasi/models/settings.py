from odoo import api, fields, models

class Settings(models.TransientModel):
	_inherit = 'res.config.settings'

	#Simpanan
	max_simp_pokok = fields.Char(string="Maksimal Simpanan Pokok")
	potongan_simp_wajib = fields.Char(string="Maksimal Simpanan Wajib")
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

		#Simpanan Pokok
		self.env['ir.config_parameter'].set_param('koperasi.max_simp_pokok', self.max_simp_pokok)
		self.env['ir.config_parameter'].set_param('koperasi.potongan_simp_wajib', self.potongan_simp_wajib)
		self.env['ir.config_parameter'].set_param('koperasi.cost_adm_member_out', self.cost_adm_member_out)

		#Pinjaman reguler
		self.env['ir.config_parameter'].set_param('koperasi.max_pinj_reguler', self.max_pinj_reguler)
		self.env['ir.config_parameter'].set_param('koperasi.pinj_reguler_pengurus', self.pinj_reguler_pengurus)
		self.env['ir.config_parameter'].set_param('koperasi.pinj_reguler_anggota', self.pinj_reguler_anggota)

		#Pinjaman Barang
		self.env['ir.config_parameter'].set_param('koperasi.max_pinj_barang', self.max_pinj_barang)
		self.env['ir.config_parameter'].set_param('koperasi.pinj_barang_pengurus', self.pinj_barang_pengurus)
		self.env['ir.config_parameter'].set_param('koperasi.pinj_barang_anggota', self.pinj_barang_anggota)
		return res

	@api.model
	def get_values(self):
		res = super(Settings, self).get_values()
		ICPSudo = self.env['ir.config_parameter'].sudo()
		#Simpanan 
		max_simp_pokok = ICPSudo.get_param('koperasi.max_simp_pokok')
		potongan_simp_wajib = ICPSudo.get_param('koperasi.potongan_simp_wajib')
		cost_adm_member_out = ICPSudo.get_param('koperasi.cost_adm_member_out')

		#Pinjaman reguler
		max_pinj_reguler = ICPSudo.get_param('koperasi.max_pinj_reguler')
		pinj_reguler_pengurus = ICPSudo.get_param('koperasi.pinj_reguler_pengurus')
		pinj_reguler_anggota = ICPSudo.get_param('koperasi.pinj_reguler_anggota')

		#Pinjaman Barang
		max_pinj_barang = ICPSudo.get_param('koperasi.max_pinj_barang')
		pinj_barang_pengurus = ICPSudo.get_param('koperasi.pinj_barang_pengurus')
		pinj_barang_anggota = ICPSudo.get_param('koperasi.pinj_barang_anggota')

		res.update(
			max_simp_pokok = max_simp_pokok,
			potongan_simp_wajib = potongan_simp_wajib,
			cost_adm_member_out = cost_adm_member_out,
			max_pinj_reguler = max_pinj_reguler,
			pinj_reguler_pengurus = pinj_reguler_pengurus,
			pinj_reguler_anggota = pinj_reguler_anggota,
			max_pinj_barang = max_pinj_barang,
			pinj_barang_pengurus = pinj_barang_pengurus,
			pinj_barang_anggota = pinj_barang_anggota
		)
		return res