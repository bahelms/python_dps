import unittest
from datetime import datetime
from dps.models.specatt import Specatt

class SpecattTest(unittest.TestCase):
    def setUp(self):
        source_data = {
            "sadlcd": None,
            "sadiv": "ABC",
            "saspec": "12",
            "sadesc": "stuff"
            }
        self.active_record = Specatt(**source_data)
        self.deleted_record = Specatt(**{**source_data, **{"sadlcd": "D"}})

    def test_source_is_transformed_to_public_data(self):
        expected_data = {
            "division": "ABC",
            "code": "12",
            "description": "stuff",
            }
        self.assertEqual(self.active_record.transform_public(), expected_data)

if __name__ == "__main__":
    unittest.main()
