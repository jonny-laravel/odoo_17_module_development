from odoo import fields,models,api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class mastermarga(models.Model):
    #_inherit = 'res.partner'
    _name = "master.marga"
    _description = "Marga Batak"
    marga = fields.Char(string='Nama Marga')
    active=fields.Boolean(default=True)