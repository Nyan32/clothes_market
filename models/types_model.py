from odoo import models, fields


class TypesModel(models.Model):
    _name = "clothes_market.types"
    _description = "Save cloth's type"

    name = fields.Char(required=True, string="Type's Name", size=50)
