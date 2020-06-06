from odoo import api, fields, models

class Koperasi(models.TransientModel):
	_inherit = 'res.config.settings'
	_name = 'koperasi.setting'