from .p135 import min_path_sum, Node

def test_p135_1():
    node = Node(10)
    assert(min_path_sum(node) == 10)


def test_p135_2():
    node = Node(10, Node(5), Node(5))
    assert(min_path_sum(node) == 15)

def test_p135_3():
    node = Node(10, Node(5, None, Node(2)), Node(5))
    assert(min_path_sum(node) == 15)

def test_p135_4():
    node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1)))
    assert(min_path_sum(node) == 16)

def test_p135_5():
    node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1), None)))
    assert(min_path_sum(node) == 15)
