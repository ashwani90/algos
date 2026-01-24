
**Explanation:**
Build a tree where each node holds the sum of a segment of the array. Queries recursively combine results.

---

### 2. **Update an Element in Segment Tree**

**Problem:**
After building the segment tree for sum queries, update an element and maintain the tree.

```python
def update(self, idx, val):
    self._update(0, self.n - 1, idx, val, 0)

def _update(self, start, end, idx, val, index):
    if start == end:
        self.tree[index] = val
        return
    mid = (start + end) // 2
    if idx <= mid:
        self._update(start, mid, idx, val, 2*index + 1)
    else:
        self._update(mid+1, end, idx, val, 2*index + 2)
    self.tree[index] = self.tree[2*index + 1] + self.tree[2*index + 2]

# Use:
seg_tree.update(1, 10)
print(seg_tree.query(1, 3))  # Output: 22 (10 + 5 + 7)
```

**Explanation:**
Update the tree by changing the leaf and re-calculating parent sums.

---

### 3. **Range Minimum Query (RMQ)**

**Problem:**
Build a segment tree to find the minimum value in a range.

```python
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
```

**Explanation:**
Similar structure as sum, but nodes store minimum of their segment.

---

### 4. **Range Maximum Query**

**Problem:**
Build a segment tree to find maximum value in a range.

(Similar to RMQ, replace `min` with `max`.)

---

### 5. **Count of Even Numbers in a Range**

**Problem:**
Build a segment tree to count how many even numbers are present in a given range.

```python
class SegmentTreeEvenCount:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, self.n -1, 0)

    def build(self, arr, start, end, index):
        if start == end:
            self.tree[index] = 1 if arr[start] % 2 == 0 else 0
            return
        mid = (start + end)//2
        self.build(arr, start, mid, 2*index + 1)
        self.build(arr, mid+1, end, 2*index + 2)
        self.tree[index] = self.tree[2*index + 1] + self.tree[2*index + 2]

    def query(self, qs, qe):
        return self._query(0, self.n - 1, qs, qe, 0)

    def _query(self, start, end, qs, qe, index):
        if qs > end or qe < start:
            return 0
        if qs <= start and qe >= end:
            return self.tree[index]
        mid = (start + end)//2
        left = self._query(start, mid, qs, qe, 2*index + 1)
        right = self._query(mid+1, end, qs, qe, 2*index + 2)
        return left + right

arr = [2, 3, 6, 8, 5]
seg_tree_even = SegmentTreeEvenCount(arr)
print(seg_tree_even.query(1, 4))  # Output: 2 (6 and 8 are even)
```

---

### 6. **Update Element to Odd/Even and Query Even Count**

Use the same tree as above, but with update function similar to problem 2.

---

### 7. **Range XOR Query**

**Problem:**
Build a segment tree to find XOR of elements in a range.

```python
class SegmentTreeXOR:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, self.n - 1, 0)

    def build(self, arr, start, end, index):
        if start == end:
            self.tree[index] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, start, mid, 2*index + 1)
        self.build(arr, mid + 1, end, 2*index + 2)
        self.tree[index] = self.tree[2*index + 1] ^ self.tree[2*index + 2]

    def query(self, qs, qe):
        return self._query(0, self.n - 1, qs, qe, 0)

    def _query(self, start, end, qs, qe, index):
        if qs > end or qe < start:
            return 0
        if qs <= start and qe >= end:
            return self.tree[index]
        mid = (start + end)//2
        left = self._query(start, mid, qs, qe, 2*index + 1)
        right = self._query(mid + 1, end, qs, qe, 2*index + 2)
        return left ^ right

arr = [3, 8, 2, 6, 4]
seg_tree_xor = SegmentTreeXOR(arr)
print(seg_tree_xor.query(1, 3))  # Output: 12 (8 ^ 2 ^ 6)
```

---

### 8. **Number of Odd Numbers in a Range**

(Similar to problem 5 but count odd numbers instead.)

---

### 9. **Find the Sum of Squares in a Range**

Build a segment tree that stores sum of squares of elements for each segment.

---

### 10. **Range Sum with Lazy Propagation for Range Updates**

**Problem:**
Efficiently perform updates on a range (e.g., add a value to all elements in a range) and query sum.

*(This is an introductory lazy propagation problem, useful once you know basic segment tree.)*

---

If you want, I can provide full code with explanations for any of the above problems or the lazy propagation approach!

---

Would you like me to proceed with full code + explanation for any of these?
