import odoo
from odoo.tests.common import TransactionCase


class TestSuppliersModel(TransactionCase):
    def setUp(self):
        super(TestSuppliersModel, self).setUp()

    def test_create(self):
        model = self.env['clothes_market.suppliers']
        req = {
            "success": {
                "name": "Louis"
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

        test_suppliers = [
            {
                "name": "Global Lover"
            },
            {
                "name": 'Silk Touche'
            },
        ]

        suppliers_model = env['clothes_market.suppliers']
        suppliers_records = suppliers_model.create(test_suppliers)

        search_domain = [("id", "=", suppliers_records[0]['id'])]

        search_results = suppliers_model.search(search_domain)

        # Assert the results
        self.assertEqual(
            search_results, suppliers_records.filtered_domain(search_domain))
