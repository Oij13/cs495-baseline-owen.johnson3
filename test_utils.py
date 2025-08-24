import unittest
from utils import first_unique_char

class TestStringMethods(unittest.TestCase):

    def test_single_unique(self):
        self.assertEqual(first_unique_char("ssffffef"),6)

    def test_no_unique(self):
        self.assertEqual(first_unique_char("aabbdd"),-1)

    def test_no_string(self):
        self.assertEqual(first_unique_char(""),-1)

    def test_all_unique(self):
        self.assertEqual(first_unique_char("abc"),0)

if __name__ == "__main__":
    unittest.main()