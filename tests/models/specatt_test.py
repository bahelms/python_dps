import unittest
from datetime import datetime
from dps.models.specatt import Specatt

class SpecattTest(unittest.TestCase):
    def setUp(self):
        source_data = {
            "sadlcd": None,
            "sadiv": "ABC",
            "sacode": "12",
            "sadesc": "stuff"
            }
        self.active_record = Specatt(**source_data)
        self.deleted_record = Specatt(**{**source_data, **{"sadlcd": "D"}})

    def test_source_is_transformed_to_public_data(self):
        expected_data = {
            "division": "ABC",
            "code": "12",
            "description": "stuff",
            "deleted_at": None
            }
        self.assertEqual(self.active_record.transform_public(), expected_data)

    def test_delete_code_transforms_into_deleted_at_date(self):
        result = self.deleted_record.transform_public()["deleted_at"]
        self.assertEqual(result, datetime.today())

    def test_is_delete(self):
        self.assertEqual(False, self.active_record.is_delete())
        self.assertEqual(True, self.deleted_record.is_delete())

if __name__ == "__main__":
    unittest.main()
