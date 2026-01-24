"""
Find Even numbers in range
"""

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4*self.n)
        self.build(arr, 0, self.n-1, 0)
    
    def build(self, arr, start, end, index):
        if start == end:
            self.tree[index] = 1 if arr[start]%2 == 0 else 0
            return 
        
        mid = (start+end)//2
        self.build(arr, start, mid, 2*index+1)
        self.build(arr, mid+1, end, 2*index+2)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

    
    def query(self, qs, qe):
        return self._query(0, self.n-1, qs, qe, 0)
    
    def _query(self, start, end, qs, qe, index):
        if qs > end or qe < start:
            return 0
        
        if qs <= start and qe >= end:
            return self.tree[index]
        
        mid = (start+end)//2
        left = self._query(start, mid, qs,qe,2*index+1)
        right = self._query(mid+1, end, qs,qe,2*index+2)
        return left+right
    
arr = [2, 3, 6, 8, 5]
seg_tree_even = SegmentTreeEvenCount(arr)
print(seg_tree_even.query(1, 4))