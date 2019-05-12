
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'<Node: value={self.value}, left={self.left}, right={self.right}>'


def get_path(root, value):
    path = [root]

    while True:
        node = path[-1]

        if value < node.value:
            if not node.left:
                return None
            path.append(node.left)
        elif value > node.value:
            if not node.right:
                return None
            path.append(node.right)
        else:
            return path

def get_most_left(node):
    while node and node.left:
        node = node.left
    return node

def get_next_bigger(root, value):
    if not root:
        return None

    path = get_path(root, value)
    if not path:
        return None
    
    node = path[-1]
    most_left_of_right = get_most_left(node.right)
    if most_left_of_right:
        return most_left_of_right

    for parent in path[:-1][::-1]:
        if parent.left:
            return parent
    
    return None
