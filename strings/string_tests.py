import unittest
from strings import *

class TestIntStringConversion(unittest.TestCase):
    def test_int_to_string(self):
        self.assertEqual(int_to_string(314), '314')
        self.assertEqual(int_to_string(-314), '-314')

    def test_string_to_int(self):
        self.assertEqual(string_to_int('123'), 123)
        self.assertEqual(string_to_int('-123'), -123)
