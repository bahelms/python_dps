import unittest
from dps.sanitizer import sanitize

class SanitizerTest(unittest.TestCase):
    def setUp(self):
        self.record = {
            1: "  Bob's Burgers   ",
            2: "  hey",
            3: "there   ",
            4: " ",
            5: "WHaT?"
            }

    def test_surrounding_whitespace_is_removed(self):
        self.assertEqual("bob's burgers", sanitize(self.record)[1])
        self.assertEqual("hey", sanitize(self.record)[2])
        self.assertEqual("there", sanitize(self.record)[3])

    def test_empty_strings_are_converted_to_None(self):
        self.assertEqual(None, sanitize(self.record)[4])

    def test_all_characters_are_lowercased(self):
        self.assertEqual("what?", sanitize(self.record)[5])

if __name__ == "__main__":
    unittest.main()
