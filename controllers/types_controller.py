from odoo import http
from odoo.http import request, Response
from odoo.exceptions import MissingError
import json


class TypesController(http.Controller):
    @http.route('/clothes_market/backend/types_controller/create', auth='public', type='http', methods=['post'], csrf=False)
    def create(self, **kw):
        req = request.httprequest.data
        req = json.loads(req)

        types_module = request.env['clothes_market.types']

        req['name'] = req['name'].lower()

        types_module.create(req)

    @http.route('/clothes_market/backend/types_controller/retrieve', auth='public', type='http', methods=['get'])
    def retrieve(self, **kw):
        output = []
        search_condition = []

        req_id = kw.get('type_id')

        if req_id != None:
            search_condition.append(('id', '=', int(req_id)))

        types_list = request.env['clothes_market.types'].search(
            search_condition)

        for type in types_list:
            id = type['id']
            name = type['name']
            output.append({'type_id': id, 'type_name': name})

        headers = {'Content-Type': 'application/json'}
        return Response(json.dumps(output), headers=headers)

    @http.route('/clothes_market/backend/types_controller/update', auth='public', type='http', methods=['post'], csrf=False)
    def update(self, **kw):
        req = request.httprequest.data
        req = json.loads(req)

        types_module = request.env['clothes_market.types']

        req_id = req['id']

        old_data_list = types_module.search([('id', '=', int(req_id))])

        if len(old_data_list) < 1:
            raise MissingError("Type with given ID is not found")

        req['name'] = req['name'].lower()

        old_data_list.write(req)

    @http.route('/clothes_market/backend/types_controller/delete', auth='public', type='http', methods=['post'], csrf=False)
    def delete(self, **kw):
        req = request.httprequest.data
        req = json.loads(req)

        types_module = request.env['clothes_market.types']

        req_id = req['id']

        target_delete = types_module.search([('id', '=', int(req_id))])
        if len(target_delete) < 1:
            raise MissingError("Type with given ID is not found")

        target_delete.unlink()
