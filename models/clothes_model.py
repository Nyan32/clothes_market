from odoo import models, fields


class ClothesModel(models.Model):
    _name = "clothes_market.clothes"
    _description = "Save clothes"

    code = fields.Char(required=True, string="Cloth's Code", size=50)
    name = fields.Char(required=True, string="Cloth's Name", size=50)
    buy_price = fields.Integer(required=True, string="Cloth's Price")

    type_id = fields.Many2one(
        comodel_name="clothes_market.types", ondelete="restrict", string="Cloth's Type", required=True)
    supplier_id = fields.Many2one(
        comodel_name="clothes_market.suppliers", ondelete="restrict", string="Cloth's Supplier", required=True)
