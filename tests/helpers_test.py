import unittest
from dps.helpers import *

class HelpersTest(unittest.TestCase):
    def test_extract_table_name(self):
        table = extract_table_name("data/some_table.csv", "data")
        self.assertEqual(table, "some_table")

    @unittest.skip("pending")
    def test_classify(self):
        pass

if __name__ == "__main__":
    unittest.main()
