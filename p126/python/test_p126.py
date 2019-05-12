from .p126 import rotate

def test_p126_rotate():
    l = [1, 2, 3, 4, 5, 6]
    rotate(l, 2)
    assert l == [3, 4, 5, 6, 1, 2]
