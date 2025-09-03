from odoo import api, fields,models

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description="Estate Property Tags"
    name=fields.Char(required=True)

    _sql_constraints = [
        ('check_name_unique', 'unique(name)',
         'The Tag Name must be Unique.')
    ]

    @api.onchange("name")
    def _upper_name (self):
        if self.name:
            self.name=self.name.upper()