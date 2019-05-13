from .p77 import merge

def test_p77_merge():
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    assert merge(intervals) == [(1, 3), (4, 10), (20, 25)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    assert merge(intervals) == [(1, 3), (4, 10), (20, 27)]
