from epi.linked_list_proto import *

def merge_two_sorted_lists(L1, L2):
    """Merge two sorted lists"""
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
    """Given a list and start and end indices, reverse the sublist between
    start and end, inclusive"""
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

def has_cycle(head):
    """Determine if list has a cycle, return start of cycle"""
    def cycle_len(end):
        start, step = end, 0
        while True:
            start = start.next
            step += 1
            if start is end:
                return step

    slow = fast = head

    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # fast goes twice as fast as slow, meaning that when they match,
            # both iterators will be in the middle of the cycle (roughly)
            # so, get two iterators, offset them by cycle length, and step
            # forward equally until they match. This must be the start of the
            # cycle.

            cycle_len_it = head
            for _ in range(cycle_len(slow)):
                cycle_len_it = cycle_len_it.next

            it = head
            while it is not cycle_len_it:
                it = it.next
                cycle_len_it = cycle_len_it.next
            return it

    return None

def overlapping_no_cycle_lists(L1, L2):
    """Determine if L1, L2 overlap, return first node where they do"""
    # get lengths, offset longer list by difference
    def get_length(L):
        length = 0
        while L:
            length += 1
            L = L.next

        return length

    len_1, len_2 = get_length(L1), get_length(L2)
    if len_1 > len_2:
        L1, L2 = L2, L1 # make L2 the longer list

    for _ in range(abs(len_2 - len_1)):
        L2 = L2.next

    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    return L1

def remove_kth_last(L, k):
    """Remove the kth to last node from L, without finding len(L)"""
    head = ListNode(0, L)

    # two iterators, offset them by k!
    first = head.next
    for _ in range(k):
        first = first.next

    second = head
    while first:
        first, second = first.next, second.next
    # first is at the end,
    # second is (k+1) from the end
    second.next = second.next.next

    return head.next
