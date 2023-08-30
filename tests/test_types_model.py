import odoo
from odoo.tests.common import TransactionCase


class TestTypesModel(TransactionCase):
    def test_create(self):
        model = self.env['clothes_market.types']
        req = {
            "success": {
                "name": "chennille"
            }
        }

        # success
        output_success = model.create(req['success'])

        self.assertEqual(
            {
                "name": output_success['name']
            },
            req['success']
        )

    def test_search(self):
        env = self.env(cr=None, context={})

        test_types = [
            {
                "name": "chennille"
            },
            {
                "name": 'chiffon'
            },
        ]

        types_model = env['clothes_market.types']
        types_records = types_model.create(test_types)

        search_domain = [("id", "=", types_records[0]['id'])]

        search_results = types_model.search(search_domain)

        # Assert the results
        self.assertEqual(
            search_results, types_records.filtered_domain(search_domain))
