import odoo
from odoo.tests.common import TransactionCase


class TestClothesModel(TransactionCase):
    def test_create(self):
        model = self.env['clothes_market.clothes']
        req = {
            "success": {
                "code": "SRM-201",
                "name": "Smooth Criminal v1",
                "buy_price": 20000,
                "type_id": 1,
                "supplier_id": 1
            }
        }

        # success
        output_success = model.create(req['success'])

        self.assertEqual(
            {
                "code": output_success['code'],
                "name": output_success['name'],
                "buy_price": output_success['buy_price'],
                "type_id": output_success['type_id']['id'],
                "supplier_id": output_success['supplier_id']['id']
            },
            req['success']
        )

    def test_search(self):
        env = self.env(cr=None, context={})

        test_clothes = [
            {
                "code": "SRM-210",
                "name": "Smooth Criminal v10",
                "buy_price": 20000,
                "type_id": 1,
                "supplier_id": 1
            },
            {
                "code": "BUF-001",
                "name": "Buffon v1",
                "buy_price": 15000,
                "type_id": 1,
                "supplier_id": 1
            },
        ]

        clothes_model = env['clothes_market.clothes']
        clothes_records = clothes_model.create(test_clothes)

        search_domain = [("id", "=", clothes_records[0]['id'])]

        search_results = clothes_model.search(search_domain)

        # Assert the results
        self.assertEqual(
            search_results, clothes_records.filtered_domain(search_domain))
