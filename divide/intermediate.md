Absolutely! Here are 10 more **harder divide and conquer problems** with solutions and detailed explanations:

---

### 21. **Count Smaller Elements After Self**

**Problem:**
Given an array `nums`, for each element, count how many elements to its right are smaller than it.

**Solution:**

```python
def count_smaller(nums):
    counts = [0] * len(nums)
    
    def merge_sort(enum):
        mid = len(enum) // 2
        if mid:
            left, right = merge_sort(enum[:mid]), merge_sort(enum[mid:])
            m, n = len(left), len(right)
            i = j = 0
            merged = []
            while i < m or j < n:
                if j == n or (i < m and left[i][1] <= right[j][1]):
                    merged.append(left[i])
                    counts[left[i][0]] += j
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            return merged
        else:
            return enum

    merge_sort(list(enumerate(nums)))
    return counts

nums = [5, 2, 6, 1]
print(count_smaller(nums))  # Output: [2, 1, 1, 0]
```

**Explanation:**
We use a modified merge sort. While merging two halves, for each element in the left half, we count how many elements in the right half are smaller and have been placed before it.

---

### 22. **Count Range Sum**

**Problem:**
Given an integer array `nums` and two integers `lower` and `upper`, count the number of range sums that lie in `[lower, upper]`.

A range sum `S(i, j)` is the sum of the elements from index i to j inclusive.

**Solution:**

```python
def countRangeSum(nums, lower, upper):
    prefix_sums = [0]
    for num in nums:
        prefix_sums.append(prefix_sums[-1] + num)

    def merge_sort(lo, hi):
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        count = merge_sort(lo, mid) + merge_sort(mid, hi)
        j = k = mid
        temp = []
        r = mid
        for left in prefix_sums[lo:mid]:
            while k < hi and prefix_sums[k] - left < lower:
                k += 1
            while j < hi and prefix_sums[j] - left <= upper:
                j += 1
            count += j - k
        prefix_sums[lo:hi] = sorted(prefix_sums[lo:hi])
        return count

    return merge_sort(0, len(prefix_sums))

nums = [-2, 5, -1]
lower, upper = -2, 2
print(countRangeSum(nums, lower, upper))  # Output: 3
```

**Explanation:**
We use prefix sums and a modified merge sort to count the number of valid ranges. The divide and conquer approach sorts prefix sums and counts valid sums during merge steps.

---

### 23. **Kth Largest Element in an Unsorted Array**

**Problem:**
Find the kth largest element in an unsorted array.

**Solution:**
(Using QuickSelect which is divide and conquer)

```python
def quick_select(nums, k):
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left
        for i in range(left, right):
            if nums[i] > pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def select(left, right, k_smallest):
        if left == right:
            return nums[left]
        pivot_index = (left + right) // 2
        pivot_index = partition(left, right, pivot_index)
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(nums) - 1, k - 1)

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(quick_select(nums, k))  # Output: 5
```

**Explanation:**
QuickSelect partitions the array and recursively searches for the kth largest element without fully sorting the array.

---

### 24. **Maximum Gap**

**Problem:**
Given an unsorted array, find the maximum difference between successive elements after sorting.

**Solution:**

```python
def maximum_gap(nums):
    if len(nums) < 2:
        return 0
    min_val, max_val = min(nums), max(nums)
    n = len(nums)
    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1

    buckets_min = [float('inf')] * bucket_count
    buckets_max = [float('-inf')] * bucket_count

    for num in nums:
        idx = (num - min_val) // bucket_size
        buckets_min[idx] = min(buckets_min[idx], num)
        buckets_max[idx] = max(buckets_max[idx], num)

    max_gap = 0
    prev_max = min_val
    for i in range(bucket_count):
        if buckets_min[i] == float('inf'):
            continue
        max_gap = max(max_gap, buckets_min[i] - prev_max)
        prev_max = buckets_max[i]

    return max_gap

nums = [3, 6, 9, 1]
print(maximum_gap(nums))  # Output: 3
```

**Explanation:**
Uses bucket sort principle dividing numbers into buckets and finding max gap between buckets, a kind of divide and conquer on value ranges.

---

### 25. **Count of Smaller Numbers After Self (Using BIT + Divide & Conquer Hybrid)**

**Note:** Already given divide & conquer variant. BIT or Fenwick Tree is another approach.

---

### 26. **Number of Islands (with Recursive DFS)**

**Problem:**
Given a 2D grid of '1's (land) and '0's (water), count the number of islands.

**Solution:**

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(num_islands(grid))  # Output: 3
```

**Explanation:**
Uses DFS to mark connected lands (islands). Recursive divide and conquer over grid neighbors.

---

### 27. **Maximum Rectangle in Histogram**

**Problem:**
Given histogram bars, find the largest rectangle area.

**Solution:** (Stack-based approach, but can be understood as divide and conquer)

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

heights = [2,1,5,6,2,3]
print(largest_rectangle_area(heights))  # Output: 10
```

**Explanation:**
Stack keeps track of bars with increasing height. When a lower bar appears, calculate area with the popped bar as height.

---

### 28. **Count Reverse Pairs**

**Problem:**
Count pairs `(i, j)` where `i < j` and `nums[i] > 2 * nums[j]`.

**Solution:**

```python
def reverse_pairs(nums):
    def merge_sort(arr):
        if len(arr) <= 1:
            return 0, arr
        mid = len(arr) // 2
        left_count, left = merge_sort(arr[:mid])
        right_count, right = merge_sort(arr[mid:])
        count = left_count + right_count

        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            count += j

        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
               
```


