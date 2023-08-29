from odoo import models, fields


class SuppliersModel(models.Model):
    _name = "clothes_market.suppliers"
    _description = "Save cloth's supplier"

    name = fields.Char(required=True, string="Supplier's Name", size=50)
