import pytest

from .p134 import SparseArray

def test_p134_1():
    arr = SparseArray([0, 0, 0], 5)

    assert arr.get(0) == 0
    assert arr.get(3) == 0

    with pytest.raises(IndexError):
        assert arr.get(-1)
        assert arr.get(-1, 0)
        assert arr.get(5)
        assert arr.set(5, 0)

    arr.set(0, 1)
    assert arr.get(0) == 1

    arr.set(4, 1)
    assert arr.get(4) == 1
