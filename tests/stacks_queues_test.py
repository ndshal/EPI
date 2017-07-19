import unittest
from epi.stacks_queues import *

class TestEvaluateRPN(unittest.TestCase):
    def test_eval_rpn(self):
        self.assertEqual(evaluate('3,4,+,2,x,1,+'), 15)

if __name__ == '__main__':
    unittest.main()
