from odoo import http
from odoo.http import request, Response
from odoo.exceptions import ValidationError, UserError, MissingError
import json


class ClothesController(http.Controller):
    @http.route('/clothes_market/backend/clothes_controller/create', auth='public', type='http', methods=['post'], csrf=False)
    def create(self, **kw):
        req = request.httprequest.data
        req = json.loads(req)

        clothes_module = request.env['clothes_market.clothes']

        if req['buy_price'] < 100:
            raise UserError("Buy price cannot be under 100")
        if clothes_module.search([("code", "=", req['code'])]):
            raise ValidationError("Code must be unique")

        clothes_module.create(req)

    @http.route('/clothes_market/backend/clothes_controller/retrieve', auth='public', type='http', methods=['get'])
    def retrieve(self, **kw):
        output = []
        search_condition = []

        req_id = kw.get('cloth_id')
        req_type_id = kw.get('type_id')

        if req_id != None:
            search_condition.append(('id', '=', int(req_id)))
        if req_type_id != None:
            search_condition.append(('type_id', '=', int(req_type_id)))

        clothes_list = request.env['clothes_market.clothes'].search(
            search_condition)

        for cloth in clothes_list:
            id = cloth['id']
            code = cloth['code']
            name = cloth['name']
            buy_price = cloth['buy_price']
            type_name = cloth['type_id']['name']
            supplier_name = cloth['supplier_id']['name']
            output.append(
                {
                    'cloth_id': id,
                    'cloth_code': code,
                    'cloth_name': name,
                    'cloth_buy_price': buy_price,
                    'cloth_type_name': type_name,
                    'cloth_supplier_name': supplier_name,
                })

        headers = {'Content-Type': 'application/json'}
        return Response(json.dumps(output), headers=headers)

    @http.route('/clothes_market/backend/clothes_controller/update', auth='public', type='http', methods=['post'], csrf=False)
    def update(self, **kw):
        req = request.httprequest.data
        req = json.loads(req)

        clothes_module = request.env['clothes_market.clothes']

        req_id = req['id']

        old_data_list = clothes_module.search([('id', '=', int(req_id))])

        if len(old_data_list) < 1:
            raise MissingError("Cloth with given ID is not found")

        old_code = old_data_list['code']
        new_code = req['code']

        if req['buy_price'] < 100:
            raise UserError("Buy price cannot be under 100")
        if clothes_module.search([("code", "=", req['code'])]) and new_code != old_code:
            raise ValidationError("Code must be unique")

        old_data_list.write(req)

    @http.route('/clothes_market/backend/clothes_controller/delete', auth='public', type='http', methods=['post'], csrf=False)
    def delete(self, **kw):
        req = request.httprequest.data
        req = json.loads(req)

        clothes_module = request.env['clothes_market.clothes']

        req_id = req['id']

        target_delete = clothes_module.search([('id', '=', int(req_id))])
        if len(target_delete) < 1:
            raise MissingError("Cloth with given ID is not found")

        target_delete.unlink()
