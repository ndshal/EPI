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

    def test_insert_after(self):
        new_node = ListNode(3)
        insert_after(self.node, new_node)
        self.assertEqual(self.node.next.data, 3)

class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        L1_values = [1, 3, 4, 6]
        L2_values = [2, 5, 10]

        self.L1 = L1_tail = ListNode()
        for l1 in L1_values:
            insert_after(L1_tail, ListNode(l1))
            L1_tail = L1_tail.next

        self.L2 = L2_tail = ListNode()
        for l2 in L2_values:
            insert_after(L2_tail, ListNode(l2))
            L2_tail = L2_tail.next

        self.L1, self.L2 = self.L1.next, self.L2.next

    def test_merge_two_lists(self):
        merged_list = merge_two_sorted_lists(self.L1, self.L2)
        self.assertEqual(to_list(merged_list), [1, 2, 3, 4, 5, 6, 10])

if __name__ == '__main__':
    unittest.main()
