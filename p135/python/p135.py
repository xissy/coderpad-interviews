
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'<Node: value={self.value}, left={self.left}, right={self.right}>'


def min_path_sum(root):
    m = float('inf')
    q = [(root, root.value)]

    while q:
        node, curr_sum = q.pop()

        if not node.left and not node.right:
            if m > curr_sum:
                m = curr_sum
            continue

        if node.left:
            q.append((node.left, curr_sum + node.left.value))
        if node.right:
            q.append((node.right, curr_sum + node.right.value))

    return m
