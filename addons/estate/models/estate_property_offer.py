from odoo import api,fields,models
from datetime import timedelta
from odoo.exceptions import UserError

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
    validity=fields.Integer(default=7,copy=False,string="Validity (days)")
    date_deadline=fields.Date(copy=False, compute="_compute_date_deadline",inverse="_inverse_date_deadline",string="DeadLine Date")

    @api.depends("create_date","validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline=record.create_date+timedelta(days=record.validity)
            else:
                record.date_deadline=fields.Date.today()+timedelta(days=record.validity)
    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline and record.create_date:
                delta=record.date_deadline-record.create_date.date()
                record.validity=delta.days
            else:
                record.validity=(record.date_deadline-fields.Date.today()).days
    def action_accept(self):
        for record in self :
            if record.property_id.state=="sold":
                raise UserError("Cannot Offer be Acccepted for Property is Sold!")
            elif record.status=="refuse":
                raise UserError("Cannot Offer be Acccepted for refuse status!")
            elif record.status=="accepted":
                raise UserError("Cannot Offer be Acccepted for twice!")
            record.status="accepted"
            record.property_id.state="sold"
            record.property_id.buyer_id=record.partner_id
            record.property_id.selling_price=record.price

        return True
    def action_refuse(self):
        for record in self:
            if record.property_id.state=="sold":
                raise UserError("Cannot Offer be Refused for Property is Sold!")
            elif record.status=="refused":
                raise UserError("Cannot Offer be refused for twice!")
            record.status="refused"       
        return True