from odoo import http
from odoo.http import request, Response
from odoo.exceptions import MissingError
import json


class SuppliersController(http.Controller):
    @http.route('/clothes_market/backend/suppliers_controller/create', auth='public', type='http', methods=['post'], csrf=False)
    def create(self, **kw):
        req = request.httprequest.data
        req = json.loads(req)

        suppliers_module = request.env['clothes_market.suppliers']

        suppliers_module.create(req)

    @http.route('/clothes_market/backend/suppliers_controller/retrieve', auth='public', type='http', methods=['get'])
    def retrieve(self, **kw):
        output = []
        search_condition = []

        req_id = kw.get('supplier_id')

        if req_id != None:
            search_condition.append(('id', '=', int(req_id)))

        suppliers_list = request.env['clothes_market.suppliers'].search(
            search_condition)

        for supplier in suppliers_list:
            id = supplier['id']
            name = supplier['name']
            output.append({'supplier_id': id, 'supplier_name': name})

        headers = {'Content-Type': 'application/json'}
        return Response(json.dumps(output), headers=headers)

    @http.route('/clothes_market/backend/suppliers_controller/update', auth='public', type='http', methods=['post'], csrf=False)
    def update(self, **kw):
        req = request.httprequest.data
        req = json.loads(req)

        suppliers_module = request.env['clothes_market.suppliers']

        req_id = req['id']

        old_data_list = suppliers_module.search([('id', '=', int(req_id))])

        if len(old_data_list) < 1:
            raise MissingError("Supplier with given ID is not found")

        old_data_list.write(req)

    @http.route('/clothes_market/backend/suppliers_controller/delete', auth='public', type='http', methods=['post'], csrf=False)
    def delete(self, **kw):
        req = request.httprequest.data
        req = json.loads(req)

        suppliers_module = request.env['clothes_market.suppliers']

        req_id = req['id']

        target_delete = suppliers_module.search([('id', '=', int(req_id))])
        if len(target_delete) < 1:
            raise MissingError("Supplier with given ID is not found")

        target_delete.unlink()
