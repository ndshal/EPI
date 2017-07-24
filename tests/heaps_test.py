import unittest
from epi.heaps import *

class TestMergeSortedArrays(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        sorted_arrays = [[3, 5, 7], [0, 6], [0, 6, 28]]
        merged_result = [0, 0, 3, 5, 6, 6, 7, 28]
        self.assertEqual(merge_sorted_arrays(sorted_arrays), merged_result)

class TestSortApproxSortedArray(unittest.TestCase):
    def test_sort_approx_sorted_array(self):
        self.assertEqual(sort_k_sorted_array([3, -1, 2, 6, 4, 5, 8], 2), [-1, 2, 3, 4, 5, 6, 8])

if __name__ == '__main__':
    unittest.main()
