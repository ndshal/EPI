import unittest
from epi.strings import *

class TestIntStringConversion(unittest.TestCase):
    def test_int_to_string(self):
        self.assertEqual(int_to_string(314), '314')
        self.assertEqual(int_to_string(-314), '-314')

    def test_string_to_int(self):
        self.assertEqual(string_to_int('123'), 123)
        self.assertEqual(string_to_int('-123'), -123)

class TestConvertBase(unittest.TestCase):
    def test_binary_to_hex(self):
        self.assertEqual(convert_base('101101', 2, 16), '2D')

    def test_hex_to_binary(self):
        self.assertEqual(convert_base('2D', 16, 2), '101101')

    def test_decimal_to_binary(self):
        self.assertEqual(convert_base('117', 10, 2), '1110101')

    def test_binary_to_decimal(self):
        self.assertEqual(convert_base('1110101', 2, 10), '117')

class TestReplaceRemove(unittest.TestCase):
    def test_replace_and_remove(self):
        input_array = ['a','c','d','b','b','c','a']
        output_array = ['d','d','c','d','c','d','d']
        self.assertEqual(replace_and_remove(7, input_array), output_array)

class TestIsPalindromicity(unittest.TestCase):
    def test_finds_palindrome(self):
        self.assertTrue(is_palindrome('lionoil'))

    def test_ignores_nonalpha_chars(self):
        self.assertTrue(is_palindrome('Able was I, ere I saw Elba!'))
        self.assertFalse(is_palindrome('Ray a Ray'))

class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words('ram is costly'), 'costly is ram')

if __name__ == '__main__':
    unittest.main()
