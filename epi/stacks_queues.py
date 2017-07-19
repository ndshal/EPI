import collections

def evaluate(RPN_expression):
    """Evaluate string encoding an expression in Reverse Polish Notation"""
    intermediate_results = []
    DELIMETER = ','
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        'x': lambda y, x: x * y,
        '/': lambda y, x: int(x / y),
    }

    for token in RPN_expression.split(DELIMETER):
        if token in OPERATORS:
            intermediate_results.append(
                OPERATORS[token](
                    intermediate_results.pop(),
                    intermediate_results.pop()))
        else: # token is a number
            intermediate_results.append(int(token))

    return intermediate_results[-1]

def binary_tree_depth_order(tree):
    """Return an array of arrays representing depth levels in a binary tree"""
    result, curr_depth_nodes = [], collections.deque([tree])
    while curr_depth_nodes:
        next_depth_nodes, this_level = collections.deque([]), []
        while curr_depth_nodes:
            curr = curr_depth_nodes.popleft()
            if curr:
                this_level.append(curr.data)
                next_depth_nodes += [curr.left, curr.right]

        if this_level:
            result.append(this_level)

        curr_depth_nodes = next_depth_nodes

    return result
