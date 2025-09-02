from odoo import _, api,fields,models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    name = fields.Char("Property Name",required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date("Available From",copy=False,default=lambda self: fields.datetime.now()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly = True,copy =False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ('north','North'),
            ('south','South'),
            ('east','East'),
            ('west','West'),
        ]
    )
    active=fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('new','New'),
            ('over_received','Offer Received'),
            ('over_accepted','Offer Accepted'),
            ('sold','Sold'),
            ('cancelled','Cancelled'),
        ],
        default='new',copy = False,required = True,
    )
    property_type_id=fields.Many2one("estate.property.type", string="Property Type")
    #user_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    salesperson_id=fields.Many2one('res.users',string='Salesman',index=True,default=lambda self: self.env.user)
    buyer_id=fields.Many2one('res.partner', string ='Buyer',index=True, copy=False)
    tag_ids=fields.Many2many('estate.property.tag', string ='Tags',index=True, copy=False)
    offer_ids=fields.One2many("estate.property.offer","property_id", string="Offer",copy=False)
    total_area=fields.Float(compute="_compute_total_area",copy=False, string="Total Area (sqm)")
    best_price=fields.Float(compute="_compute_best_price", copy=False, string="Best Offer")
    

    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = sum([record.living_area,record.garden_area])
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price=max(record.offer_ids.mapped("price"))
            else:
                record.best_price=0.0
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            
            self.garden_area=10
            self.garden_orientation="north"
            return {'warning': {
                'title': _("Info"),
                'message': ('This option enable Garden Area(default=10) and Garden Orientation (default=north)')}}
        else:
            
            self.garden_area=None
            self.garden_orientation=None
            return {'warning': {
                'title': _("Info"),
                'message': ('This option will enable Garden Area set to 0 and Garden Orientation set to blank ')}}