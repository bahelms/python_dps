import unittest
from dps.transformer import transform

class TransformerTest(unittest.TestCase):
    def setUp(self):
        self.source_table = "specatt"
        self.source_data = {
            "SADLCD": None,
            "SADIV": "ABC",
            "SACODE": "12",
            "SADESC": "stuff"
            }
        self.deleted_data = {"SACODE": "98", "SADLCD": "D"}

    def test_source_is_transformed_to_public_data(self):
        expected_data = {
            "division": "ABC",
            "code": "12",
            "description": "stuff",
            "deleted_at": None
            }
        result = transform(self.source_data, self.source_table)
        self.assertEqual(result, expected_data)

    def test_delete_code_transforms_into_deleted_at_date(self):
        expected_data = {"code": "98", "deleted_at": ""}
        result = transform(self.deleted_data, self.source_table)
        self.assertEqual(result, expected_data)

if __name__ == "__main__":
    unittest.main()
