import unittest
import random
from arrays import *

class TestDutchFlagPartition(unittest.TestCase):
    def setUp(self):
        a = list(range(0,10))
        random.shuffle(a)
        self.pivot = random.randint(0,9)
        pivot_index = a.index(self.pivot)
        self.paritioned = dutch_flag_partition(pivot_index, a)

    def test_less_than_pivot(self):
        left = self.paritioned[:self.paritioned.index(self.pivot)]
        less_than = map(lambda x: x < self.pivot, left)
        self.assertTrue(all(less_than))

    def test_greater_than_pivot(self):
        right = self.paritioned[self.paritioned.index(self.pivot) + 1:]
        greater_than = map(lambda x: x > self.pivot, right)
        self.assertTrue(all(greater_than))

if __name__ == '__main__':
    unittest.main()
