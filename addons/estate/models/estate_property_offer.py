from odoo import fields,models

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Estate Property Offer"
    price=fields.Float(string="The Prices")
    status=fields.Selection(
        selection=[
            ('accepted','Accepted'),
            ('refused','Refused'),
        ],copy=False
    )
    partner_id=fields.Many2one("res.partner",string="Partner",required=True,copy=False)
    property_id=fields.Many2one("estate.property",string="Property",required=True,copy=False)
