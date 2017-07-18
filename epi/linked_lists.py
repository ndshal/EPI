class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

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
