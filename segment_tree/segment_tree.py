"""

Given an array, build a segment tree to answer sum queries over any range efficiently.
"""

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4*self.n)
        self.build(arr, 0, self.n-1, 0)

    def build(self, arr, start, end, index):
        if start == end:
            self.tree[index] = arr[start]
            return
        
        mid = (start+end)//2
        self.build(arr, start, end, 2*index+1)
        self.build(arr, start, end, 2*index+2)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]
    
    def query(self, qs, qe):
        self._query(0, self.n-1, qs, qe, 0)
    
    def _query(self, start, end, qs, eq, index):
        if qs > end or qe < start:
            return 0
        
        if qs <= start and qe >= end:
            return self.tree[index]
        
        mid = (start+end)//2
        left = self._query(start, mid, qs, qe, 2*index+1)
        right = self._query(mid+1, end, qs, qe, 2*index+2)
        return left+right

arr = [1,3,5,7,9,11]
seg_tree = SegmentTree(arr)
print(seg_tree.query(1, 3))