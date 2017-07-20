import collections

def is_balanced_binary_tree(tree):
    """Determine if a binary tree is balanced"""

    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced

def is_symmetric(tree):
    """Determine if a binary tree is symmetric"""

    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data and
                    check_symmetric(subtree_0.left, subtree_0.right) and
                    check_symmetric(subtree_1.left, subtree_1.right))
        return False # one is empty, the other is not

    return not tree or check_symmetric(tree.left, tree.right)

def lca(node_0, node_1):
    """Compute the LCA when nodes have parent pointers"""

    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent

        return depth

    # start at same depth, traverse up till equal
    depth_0, depth_1 = get_depth(node_0), get_depth(node_1)
    if depth_1 > depth_0:
        node_0, node_1 = node_1, node_0

    depth_diff = abs(depth_0 - depth_1)
    while depth_diff:
        node_0 = node_0.parent
        depth_diff -= 1

    while node_0 is not node_1:
        node_0, node_1 = node_0.parent, node_1.parent

    return node_0
