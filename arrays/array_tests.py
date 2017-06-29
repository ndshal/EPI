import unittest
import random
from arrays import *

class TestDutchFlagPartition(unittest.TestCase):
    def setUp(self):
        self.a = list(range(0,10))
        random.shuffle(self.a)
        # generate a random number to be the pivot, then find it in the list
        self.i = self.a.index(random.randint(0,9))

    def test_less_than_pivot(self):
        left = dutch_flag_partition(self.i, self.a)[:self.i]
        less_than = map(lambda x: x < self.a[self.i], left)
        self.assertTrue(all(less_than))

    def test_greater_than_pivot(self):
        right = dutch_flag_partition(self.i, self.a)[self.i + 1:]
        greater_than = map(lambda x: x >= self.a[self.i], right)
        self.assertTrue(all(greater_than))

if __name__ == '__main__':
    unittest.main()
