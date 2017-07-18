class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def to_list(L):
    res = []
    while L:
        res.append(L.data)
        L = L.next

    return res

def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L

def insert_after(node, next_node):
    next_node.next = node.next
    node.next = next_node


def delete(node):
    node.data = node.next.data
    node.next = node.next.next

def delete_after(node):
    node.next = node.next.next

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
