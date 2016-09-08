import unittest
from dps.helpers import *
from dps.models.specatt import Specatt

class HelpersTest(unittest.TestCase):
    def test_extract_table_name(self):
        table = extract_table_name("data/some_table.csv", "data")
        self.assertEqual(table, "some_table")

    def test_classify(self):
        self.assertEqual(classify("dps.models.specatt", "Specatt"), Specatt)

if __name__ == "__main__":
    unittest.main()
