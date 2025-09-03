from odoo import api,fields,models

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description="Estate Property Type"
    name=fields.Char(required=True)

    _sql_constraints = [
        ('check_name_unique', 'unique(name)',
         'The Type  Name must be Unique.')
    ]

    @api.onchange("name")
    def _upper_name (self):
        if self.name:
            self.name=self.name.upper()