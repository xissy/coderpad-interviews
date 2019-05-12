
class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        self.map = {}

        orig_arr_size = len(arr)
        for i, e in enumerate(arr):
            if i >= orig_arr_size:
                break
            if e != 0:
                map[i] = e
    
    def set(self, i, val):
        if i >= self.size:
            raise IndexError()

        self.map[i] = val

    def get(self, i):
        if i >= self.size:
            raise IndexError()

        v = self.map.get(i)
        if v is None:
            return 0
        return v
