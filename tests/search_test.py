import unittest
from epi.search import *

class TestFindFirstOccurence(unittest.TestCase):
    def test_search_first_of_k(self):
        self.assertEqual(search_first_of_k(
            [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 103), 3)

if __name__ == '__main__':
    unittest.main()
