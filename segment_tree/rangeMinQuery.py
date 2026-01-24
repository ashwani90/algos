"""
Range min query using Segment tree
"""

class SegmentTreeMin:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        self.build(arr, 0, self.n-1, 0)

    def build(self, arr, start, end, index):
        if start == end:
            self.tree[index] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, start, mid, 2*index+1)
        self.build(arr, mid+1, end, 2*index+2)
        self.tree[index] = min(self.tree[2*index+1], self.tree[2*index+2])

    def query(self, qs, qe):
        return self._query(0, self.n-1, qs, qe, 0)

    def _query(self, start, end, qs, qe, index):
        if qs > end or qe < start:
            return float('inf')
        if qs <= start and qe >= end:
            return self.tree[index]
        mid = (start + end) // 2
        left = self._query(start, mid, qs, qe, 2*index+1)
        right = self._query(mid+1, end, qs, qe, 2*index+2)
        return min(left, right)

arr = [2, 5, 1, 4, 9, 3]
seg_tree_min = SegmentTreeMin(arr)
print(seg_tree_min.query(1, 4))  # Output: 1 (minimum in range)