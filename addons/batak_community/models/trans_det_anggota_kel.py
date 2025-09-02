from odoo import fields,models

class TransDetAnggotaKel(models.Model):
    _name="trans.det.anggota.kel"
    _description="Transaksi Detail Anggota Keluarga"
    name=fields.Char(required=True,string="Nama Anggota Keluarga")
    det_marga_id=fields.Many2one("master.marga",string='Marga',required=True,index=True,copy=False)
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    tempat_lahir = fields.Char(string='Tempat Lahir')
    jenis_kelamin = fields.Selection([('male', 'Laki-laki'), ('female', 'Perempuan')], string='Jenis Kelamin',required=True)
    status_keluarga = fields.Selection(
        selection=[
            ('suami','Suami'),
            ('istri','Istri'),
            ('anak','Anak'),
            ('tanggungan','Tanggungan'),
        ], string="Status dalam Keluarga"
    )
trans_daftar_anggota_id=fields.Many2one("trans.daftar.anggota",string="Anggota ID",required=True,copy=False)