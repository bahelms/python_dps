import unittest
from dps.transformer import transform

class TransformerTest(unittest.TestCase):
    def setUp(self):
        self.source_data = {
            "HADLCD": None,
            "HADIV": "ABC",
            "HASPEC": "12",
            "HADESC": "stuff"
            }

    def test_source_is_transformed_to_public_data(self):
        expected_data = {
            "division": "ABC",
            "code": "12",
            "description": "stuff",
            }
        self.assertEqual(transform(self.source_data), expected_data)

if __name__ == "__main__":
    unittest.main()
