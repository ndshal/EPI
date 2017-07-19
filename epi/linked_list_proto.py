class ListNode:
    """Node in a singly linked list"""

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def build_list(node_values):
    head = tail = ListNode()
    for val in node_values:
        insert_after(tail, ListNode(val))
        tail = tail.next

    return head.next

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
