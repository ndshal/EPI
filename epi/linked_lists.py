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
    return L
