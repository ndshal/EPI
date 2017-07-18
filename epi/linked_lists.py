from epi.linked_list_proto import *

def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # either L1 or L2 is None
    tail.next = L1 or L2

    return dummy_head.next

def reverse_sublist(L, start, end):
    head = sublist_head = ListNode(0, L)
    for _ in range(start):
        sublist_head = sublist_head.next

    # curr_node = sublist_tail = sublist_head.next
    # for _ in range(start, end):
    #     next_node = curr_node.next
    #     insert_after(sublist_head, curr_node)
    #     curr_node = next_node
    #
    # sublist_tail.next = next_node

    sublist_iter = sublist_head.next
    for _ in range(start, end):
        current = sublist_iter.next
        sublist_iter.next, current.next, sublist_head.next = (
            current.next, sublist_head.next, current)

    return head.next

def has_cycle(L):
    slow = fast = L
    while slow and fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            return None

        if slow == fast:
            return True

    return None
