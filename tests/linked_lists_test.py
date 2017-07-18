import unittest
from epi.linked_lists import *

class TestListNode(unittest.TestCase):
    def setUp(self):
        self.node = ListNode(1)
        self.other_node = ListNode(2)

    def test_has_data(self):
        try:
            self.node.data
        except:
            self.fail("ListNode has no data attribute")

    def test_initializes_with_no_next(self):
        self.assertEqual(self.node.next, None)

    def test_can_set_next(self):
        self.node.next = self.other_node
        self.assertEqual(self.node.next.data, 2)

if __name__ == '__main__':
    unittest.main()
