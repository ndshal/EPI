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

class TestPlusOne(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(plus_one([1,2,8]), [1,2,9])

    def test_carry_the_one(self):
        self.assertEqual(plus_one([1,2,9]), [1,3,0])

    def test_add_digit(self):
        self.assertEqual(plus_one([9,9]), [1,0,0])

if __name__ == '__main__':
    unittest.main()
