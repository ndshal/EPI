import unittest
from epi.linked_list_proto import *
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
        self.L1 = build_list([1, 3, 4, 6])
        self.L2 = build_list([2, 5, 10])

    def test_merge_two_lists(self):
        merged_list = merge_two_sorted_lists(self.L1, self.L2)
        self.assertEqual(to_list(merged_list), [1, 2, 3, 4, 5, 6, 10])

class TestReverseSublist(unittest.TestCase):
    def setUp(self):
        self.odd_list = build_list(range(1,20,2))

    def test_reverse_sublist(self):
        reverse_sublist(self.odd_list, 4, 7)
        self.assertEqual(to_list(self.odd_list), [1, 3, 5, 7, 15, 13, 11, 9, 17, 19])

if __name__ == '__main__':
    unittest.main()
