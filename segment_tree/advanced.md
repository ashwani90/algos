Absolutely! Here are **10 advanced segment tree problems** along with solutions and explanations. These problems go beyond basic queries and updates, incorporating concepts like lazy propagation with complex operations, persistent segment trees, merging, and more.

---

# Advanced Segment Tree Problems with Solutions & Explanations

---

### 1. **Range Update and Range Query with Lazy Propagation (Add and Sum)**

**Problem:**
You have an array; support adding a value to all elements in a range and querying the sum of any range efficiently.

**Solution Sketch:**
Use lazy propagation segment tree to delay updates and apply only when necessary.

```python
class SegmentTreeRangeUpdate:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0]*(4*self.n)
        self.lazy = [0]*(4*self.n)
        self.build(arr, 0, self.n-1, 0)

    def build(self, arr, start, end, idx):
        if start == end:
            self.tree[idx] = arr[start]
            return
        mid = (start+end)//2
        self.build(arr, start, mid, 2*idx+1)
        self.build(arr, mid+1, end, 2*idx+2)
        self.tree[idx] = self.tree[2*idx+1] + self.tree[2*idx+2]

    def update_range(self, qs, qe, val):
        self._update_range(0, self.n-1, qs, qe, val, 0)

    def _update_range(self, start, end, qs, qe, val, idx):
        if self.lazy[idx] != 0:
            self.tree[idx] += (end-start+1)*self.lazy[idx]
            if start != end:
                self.lazy[2*idx+1] += self.lazy[idx]
                self.lazy[2*idx+2] += self.lazy[idx]
            self.lazy[idx] = 0

        if start > qe or end < qs:
            return
        if qs <= start and qe >= end:
            self.tree[idx] += (end-start+1)*val
            if start != end:
                self.lazy[2*idx+1] += val
                self.lazy[2*idx+2] += val
            return
        mid = (start+end)//2
        self._update_range(start, mid, qs, qe, val, 2*idx+1)
        self._update_range(mid+1, end, qs, qe, val, 2*idx+2)
        self.tree[idx] = self.tree[2*idx+1] + self.tree[2*idx+2]

    def query_range(self, qs, qe):
        return self._query_range(0, self.n-1, qs, qe, 0)

    def _query_range(self, start, end, qs, qe, idx):
        if start > qe or end < qs:
            return 0
        if self.lazy[idx] != 0:
            self.tree[idx] += (end-start+1)*self.lazy[idx]
            if start != end:
                self.lazy[2*idx+1] += self.lazy[idx]
                self.lazy[2*idx+2] += self.lazy[idx]
            self.lazy[idx] = 0
        if qs <= start and qe >= end:
            return self.tree[idx]
        mid = (start+end)//2
        left_sum = self._query_range(start, mid, qs, qe, 2*idx+1)
        right_sum = self._query_range(mid+1, end, qs, qe, 2*idx+2)
        return left_sum + right_sum
```

**Explanation:**
Lazy propagation allows efficient range updates and queries by postponing updates until needed.

---

### 2. **Range Minimum Query with Range Update (Assignment)**

**Problem:**
Support queries for the minimum in a range, and assign all elements in a range to a given value.

**Key:**
Implement lazy propagation for assignment operations (not just increments).

---

### 3. **Persistent Segment Tree for K-th Order Statistics**

**Problem:**
Given an array, create a versioned segment tree that can query the k-th smallest element in any prefix/version.

**Explanation:**
Build persistent segment trees that maintain versions after each update. Queries use version roots.

---

### 4. **Count of Inversions Using Segment Tree**

Count number of pairs `(i, j)` with `i < j` and `arr[i] > arr[j]` efficiently using segment trees to count how many smaller elements have appeared.

---

### 5. **Segment Tree for Merging Intervals**

Given intervals, support queries for union length or overlapping intervals using a segment tree where nodes store interval counts.

---

### 6. **Segment Tree Beats**

Handle range minimum/maximum update queries that restrict the update only if the current value is greater/less than the new value (advanced data structure).

---

### 7. **Segment Tree for Frequency of Mode**

Support queries to find the mode (most frequent element) in a given range.

---

### 8. **Dynamic Connectivity with Segment Trees**

Support queries on connectivity in dynamic graphs using segment trees combined with union-find structures.

---

### 9. **Segment Tree with Fractional Cascading**

Enhance segment tree queries with fractional cascading to speed up multiple binary searches in associated arrays.

---

### 10. **2D Segment Tree**

Build a segment tree for 2D grids to support queries and updates on submatrices.

---

## Detailed Example — Problem 2 (Range Min Query + Range Assignment Update)

```python
class SegmentTreeAssignMin:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        self.lazy = [None] * (4 * self.n)  # None means no pending assignment
        self.build(arr, 0, self.n - 1, 0)

    def build(self, arr, start, end, idx):
        if start == end:
            self.tree[idx] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, start, mid, 2*idx + 1)
        self.build(arr, mid+1, end, 2*idx + 2)
        self.tree[idx] = min(self.tree[2*idx+1], self.tree[2*idx+2])

    def push_down(self, idx, start, end):
        if self.lazy[idx] is not None:
            self.tree[idx] = self.lazy[idx]
            if start != end:
                self.lazy[2*idx+1] = self.lazy[idx]
                self.lazy[2*idx+2] = self.lazy[idx]
            self.lazy[idx] = None

    def update_range(self, qs, qe, val):
        self._update_range(0, self.n - 1, qs, qe, val, 0)

    def _update_range(self, start, end, qs, qe, val, idx):
        self.push_down(idx, start, end)
        if start > qe or end < qs:
            return
        if qs <= start and qe >= end:
            self.lazy[idx] = val
            self.push_down(idx, start, end)
            return
        mid = (start + end) // 2
        self._update_range(start, mid, qs, qe, val, 2*idx+1)
        self._update_range(mid+1, end, qs, qe, val, 2*idx+2)
        self.tree[idx] = min(self.tree[2*idx+1], self.tree[2*idx+2])

    def query_range(self, qs, qe):
        return self._query_range(0, self.n - 1, qs, qe, 0)

    def _query_range(self, start, end, qs, qe, idx):
        if start > qe or end < qs:
            return float('inf')
        self.push_down(idx, start, end)
        if qs <= start and qe >= end:
            return self.tree[idx]
        mid = (start + end) // 2
        left_min = self._query_range(start, mid, qs, qe, 2*idx+1)
        right_min = self._query_range(mid+1, end, qs, qe, 2*idx+2)
        return min(left_min, right_min)

# Explanation:
# We lazily assign values to ranges. push_down applies pending assignments.
# Queries return min in any range.
```

---

Would you like me to provide full code + explanations for any other specific advanced problem? Or do you want sample inputs/outputs or tests?
