from odoo import fields,models,api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class BatakCommunity(models.Model):
    #_inherit = 'res.partner'
    _name = "batak.community"
    _description = "Batak Community"
    nama_keluarga = fields.Char(string='Nama Keluarga',required=True)
    
   # property_type_id=fields.Many2one("estate.property.type", string="Property Type")
    # father_id = fields.Many2one('res.partner', string='Ayah',required=True)
    #mother_id = fields.Many2one('res.partner', string='Ibu')
    #generation = fields.Integer(string='Generasi', compute='_compute_generation', store=True,required=True)
    is_anggota_aktif = fields.Boolean(string='Anggota Aktif', default=True)
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    tempat_lahir = fields.Char(string='Tempat Lahir')
    jenis_kelamin = fields.Selection([('male', 'Laki-laki'), ('female', 'Perempuan')], string='Jenis Kelamin',required=True)
    active=fields.Boolean(default=True)
    marga_id = fields.Many2one("master.marga",string='Marga')
    # Fungsi untuk otomatis menghitung generasi
    # @api.depends('father_id.generation')
    # def _compute_generation(self):
    #     for record in self:
    #         if record.father_id:
    #             record.generation = record.father_id.generation + 1
    #         else:
    #             # Jika tidak ada ayah yang ditentukan, asumsikan dia adalah leluhur (generasi 0)
    #             record.generation = 0
