import unittest
from sanitizer import sanitize

class SanitizerTest(unittest.TestCase):
    def setUp(self):
        self.record = {
            1: "  Bob's Burgers   ",
            2: "  hey",
            3: "there   ",
            4: " "
        }

    def test_whitespace_is_removed(self):
        self.assertEqual("Bob's Burgers", sanitize(self.record)[1])

    def test_empty_strings_are_converted_to_None(self):
        self.assertEqual(None, sanitize(self.record)[4])

if __name__ == "__main__":
    unittest.main()