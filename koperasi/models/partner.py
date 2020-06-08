from odoo import api, fields, models
from odoo.addons import decimal_precision as dp

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    is_member = fields.Boolean("Is Member Koperasi", default=True)
    is_active = fields.Boolean("Is Aktif", default=True)
    simp_pokok = fields.Selection([('1', '1 Kali'), ('2', '2 Kali'), ('4', '4 Kali'), ('5', '5 Kali'), ('10', '10 Kali')], 
    	'Cicilan Simpanan Pokok', default='1', required = True)
    max_simp_pokok = fields.Float(string="Max Simpanan Pokok", compute="_compute_sim_pokok", readonly=True, 
    	digits=dp.get_precision('Product Price'))
    pot_simp_wajib = fields.Float(string="Pot Simpanan Wajib", compute="_compute_sim_wajib", readonly=True,
    	digits=dp.get_precision('Product Price'))
    min_simp_sukarela = fields.Float(string="Min Simpanan Sukarela", compute="_compute_sim_sukarela", readonly=True, 
    	digits=dp.get_precision('Product Price'))

    def _compute_sim_sukarela(self):
    	for x in self:
    		x.min_simp_sukarela = self.env['ir.config_parameter'].sudo().get_param('koperasi.min_simp_sukarela')

    def _compute_sim_wajib(self):
    	for x in self:
    		x.pot_simp_wajib = self.env['ir.config_parameter'].sudo().get_param('koperasi.potongan_simp_wajib')

    def _compute_sim_pokok(self):
    	for x in self:
    		x.max_simp_pokok = self.env['ir.config_parameter'].sudo().get_param('koperasi.max_simp_pokok')