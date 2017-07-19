import unittest
from epi.binary_tree_proto import BinaryTreeNode
from epi.stacks_queues import *

class TestEvaluateRPN(unittest.TestCase):
    def test_eval_rpn(self):
        self.assertEqual(evaluate('3,4,+,2,x,1,+'), 15)

class TestBinaryTreeDepthOrder(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTreeNode(314)
        B = BinaryTreeNode(6)
        C = BinaryTreeNode(271)
        D = BinaryTreeNode(28)
        E = BinaryTreeNode(0)
        F = BinaryTreeNode(561)
        G = BinaryTreeNode(3)
        H = BinaryTreeNode(17)
        I = BinaryTreeNode(6)
        J = BinaryTreeNode(2)
        K = BinaryTreeNode(1)
        L = BinaryTreeNode(401)
        M = BinaryTreeNode(257)
        N = BinaryTreeNode(641)
        O = BinaryTreeNode(271)
        P = BinaryTreeNode(28)

        self.root.left, self.root.right = B, I
        B.left, B.right = C, F
        C.left, C.right = D, E
        F.right = G
        G.left = H
        I.left, I.right = J, O
        J.right = K
        K.left, K.right = L, N
        L.right = M
        O.right = P

    def test_tree_depth_order(self):
        expected = [
            [314],
            [6, 6],
            [271, 561, 2, 271],
            [28, 0, 3, 1, 28],
            [17, 401, 257],
            [641]
        ]
        self.assertEqual(binary_tree_depth_order(self.root), expected)

if __name__ == '__main__':
    unittest.main()
