import unittest
from dps.helpers import *

class HelpersTest(unittest.TestCase):
    def test_titleize(self):
        self.assertEqual(titleize("spec_attribute"), "SpecAttribute")
        self.assertEqual(titleize("specatt"), "Specatt")

    @unittest.skip("pending")
    def test_classify(self):
        pass

if __name__ == "__main__":
    unittest.main()
