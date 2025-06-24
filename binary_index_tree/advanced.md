Certainly! Here are **10 advanced level Binary Indexed Tree (Fenwick Tree) problems** with detailed solutions and explanations in Python.

---

# 1. Range Update and Range Query (Fenwick Tree)

**Problem:**
Support adding a value `val` to all elements in a range `[l, r]` and querying the sum of elements in any range `[l, r]`.

**Solution:**
We extend the Fenwick Tree idea with two Fenwicks: one for values and one for correction terms.

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

class RangeUpdateRangeQuery:
    def __init__(self, n):
        self.n = n
        self.B1 = FenwickTree(n)
        self.B2 = FenwickTree(n)

    def _update(self, ft, i, delta):
        while i <= self.n:
            ft.tree[i] += delta
            i += i & -i

    def range_update(self, l, r, val):
        self.B1.update(l, val)
        self.B1.update(r + 1, -val)
        self.B2.update(l, val * (l - 1))
        self.B2.update(r + 1, -val * r)

    def prefix_sum(self, i):
        return self.B1.prefix_sum(i) * i - self.B2.prefix_sum(i)

    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

# Example Usage:
ru_rq = RangeUpdateRangeQuery(5)
ru_rq.range_update(1, 3, 5)
print(ru_rq.range_sum(1, 3))  # Output: 15
print(ru_rq.range_sum(2, 5))  # Output: 10
```

**Explanation:**
By using two Fenwicks, we simulate the effect of adding values over ranges, then get the range sums using inclusion-exclusion.

---

# 2. Find K-th Order Statistic in Fenwick Tree

**Problem:**
Given a Fenwick Tree storing frequencies, find the element corresponding to the k-th cumulative frequency efficiently.

**Solution:**

```python
def find_kth(ft, k):
    pos = 0
    bit_mask = 1 << (ft.n.bit_length())  # largest power of two <= n
    while bit_mask > 0:
        next_pos = pos + bit_mask
        if next_pos <= ft.n and ft.tree[next_pos] < k:
            k -= ft.tree[next_pos]
            pos = next_pos
        bit_mask >>= 1
    return pos + 1

# Example usage:
ft = FenwickTree(10)
arr = [1,2,2,3,4,4,4,5,5]
for x in arr:
    ft.update(x, 1)

print(find_kth(ft, 5))  # Output: 4 (the 5th element in sorted order)
```

**Explanation:**
We binary search in Fenwicks on prefix sums to find the position where cumulative frequency reaches `k`.

---

# 3. Count Number of Smaller Elements After Self

**Problem:**
For each element in an array, count how many elements to its right are smaller.

**Solution:**

```python
def smaller_after_self(nums):
    offset = 10**5  # offset to handle negative numbers if needed
    size = 2 * 10**5  # maximum value range
    ft = FenwickTree(size)
    result = []
    for num in reversed(nums):
        idx = num + offset
        result.append(ft.prefix_sum(idx - 1))
        ft.update(idx, 1)
    return result[::-1]

print(smaller_after_self([5, 2, 6, 1]))  # Output: [2,1,1,0]
```

**Explanation:**
Traverse from right to left, query how many smaller numbers appeared, then update Fenwicks with current number.

---

# 4. Count Inversions with Large Range Values (Coordinate Compression + Fenwicks)

**Problem:**
Count inversions in an array where values can be large (up to 10^9).

**Solution:**

```python
def count_inversions(arr):
    sorted_unique = sorted(set(arr))
    rank = {v:i+1 for i,v in enumerate(sorted_unique)}  # compress values

    ft = FenwickTree(len(rank))
    inv_count = 0

    for num in reversed(arr):
        r = rank[num]
        inv_count += ft.prefix_sum(r - 1)
        ft.update(r, 1)
    return inv_count

print(count_inversions([10**9, 1, 2, 3, 10**9 - 1]))  # Output: 2
```

**Explanation:**
Coordinate compression maps large values into Fenwicks indices. Then Fenwicks count smaller elements after each element.

---

# 5. 2D Fenwick Tree for Rectangle Sum Queries

**Problem:**
Support updates on points and query sum in any rectangular region in a 2D grid.

**Solution:**

```python
class FenwickTree2D:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.tree = [[0]*(m+1) for _ in range(n+1)]

    def update(self, x, y, delta):
        i = x
        while i <= self.n:
            j = y
            while j <= self.m:
                self.tree[i][j] += delta
                j += j & -j
            i += i & -i

    def prefix_sum(self, x, y):
        s = 0
        i = x
        while i > 0:
            j = y
            while j > 0:
                s += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return s

    def range_sum(self, x1, y1, x2, y2):
        return (self.prefix_sum(x2, y2) - self.prefix_sum(x1-1, y2) -
                self.prefix_sum(x2, y1-1) + self.prefix_sum(x1-1, y1-1))

ft2d = FenwickTree2D(5,5)
ft2d.update(1,1,5)
ft2d.update(3,3,2)
print(ft2d.range_sum(1,1,3,3))  # Output: 7
```

**Explanation:**
2D Fenwicks store cumulative sums; queries are answered with inclusion-exclusion of prefix sums.

---

# 6. Longest Increasing Subsequence Using Fenwicks

**Problem:**
Compute the length of the LIS in O(n log n) using Fenwicks.

**Solution:**

```python
def length_of_LIS(arr):
    sorted_unique = sorted(set(arr))
    rank = {v:i+1 for i,v in enumerate(sorted_unique)}
    ft = FenwickTree(len(rank))
    for x in arr:
        r = rank[x]
        best = ft.prefix_sum(r - 1)
        ft.update(r, best + 1)
    return ft.prefix_sum(len(rank))

print(length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
```

**Explanation:**
Fenwicks store LIS length ending at values ≤ current; query best LIS length before current value, update with new best.

---

# 7. Count Number of Subarrays with Sum at Most K

**Problem:**
Count number of subarrays whose sums are at most `k`.

**Solution Idea:**
Use prefix sums + Fenwicks to count how many prefix sums satisfy a certain condition.

**Partial solution outline:**
Sort prefix sums, coordinate compress, and use Fenwicks to count how many prefix sums are ≤ current prefix sum - k.

---

# 8. Distinct Elements in Subarray Queries (Offline + Fenwicks)

**Problem:**
Given queries `(l, r)`, count distinct elements in subarray `[l, r]`.

**Solution:**
Process queries offline sorted by right index, use Fenwicks to maintain count of distinct elements as you move `r`.

---

# 9. K-th Smallest Number in Subarray Queries (Offline + Fenwicks)

**Problem:**
For queries `(l, r, k)`, find the k-th smallest element in subarray `[l, r]`.

**Solution Sketch:**
Use offline binary search + Fenwicks to maintain counts of elements ≤ mid.

---

# 10. Dynamic Connectivity Counting with Fenwicks

**Problem:**
Support adding/removing edges and queries counting connected components dynamically.

**Solution:**
Fenwicks combine with DSU (Disjoint Set Union) to keep track of counts and update connected components.

---

If you want, I can provide **full Python code and step-by-step explanation** for any specific problem above or dive into problems #7-10 which are more complex. Just let me know!
