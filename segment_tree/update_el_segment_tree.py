"""
Update a segment element tree
"""

def update(self, idx, val):
    self._update(0, self.n-1, idx, val, 0)

def _update(self, start, end, idx, val, index):
    if start == end:
        self.tree[index] = val
    
    mid = (start+end)//2
    if idx <= mid:
        self._update(start, mid, idx, val, 2*index+1)
    else:
        self._update(mid+1, end, idx, val, 2*index+2)
    self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]

seg_tree.update(1, 10)
print(seg_tree.query(1, 3))  # Output: 22 (10 + 5 + 7)