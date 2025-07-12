Continuing the solution for **Count Reverse Pairs** and then moving on with more advanced divide and conquer problems:

---

### 28. (cont.) **Count Reverse Pairs**

```python
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return count, merged

    count, _ = merge_sort(nums)
    return count

nums = [1,3,2,3,1]
print(reverse_pairs(nums))  # Output: 2
```

**Explanation:**
This uses a modified merge sort. Before merging two sorted halves, we count how many pairs satisfy `left[i] > 2 * right[j]`. Then merge them like usual.

---

### 29. **Find Median of Two Sorted Arrays**

**Problem:**
Find the median of two sorted arrays in O(log(m+n)) time.

**Solution:**

```python
def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            imax = i - 1
        else:
            if i == 0: max_left = B[j-1]
            elif j == 0: max_left = A[i-1]
            else: max_left = max(A[i-1], B[j-1])
            if (m + n) % 2 == 1:
                return max_left
            if i == m: min_right = B[j]
            elif j == n: min_right = A[i]
            else: min_right = min(A[i], B[j])
            return (max_left + min_right) / 2.0

nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0
```

**Explanation:**
Uses binary search on the smaller array to partition both arrays into halves such that left half contains smaller elements and right half contains bigger elements. Median is calculated from partition edges.

---

### 30. **Search in Rotated Sorted Array**

**Problem:**
Search a target in a rotated sorted array in O(log n).

**Solution:**

```python
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))  # Output: 4
```

**Explanation:**
Binary search adapted to handle rotation by checking sorted halves and adjusting search space.

---

### 31. **Find Peak Element**

**Problem:**
Find a peak element in an array (element greater than neighbors).

**Solution:**

```python
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))  # Output: 1 or 5 (indexes of peaks)
```

**Explanation:**
Uses binary search; if mid element > next element, peak is left side else right side.

---

### 32. **Median of a Stream**

**Problem:**
Maintain median dynamically as new elements come.

**Solution:**
Uses two heaps (max-heap for lower half, min-heap for upper half).

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (invert values)
        self.large = []  # min heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())  # 1.5
mf.addNum(3)
print(mf.findMedian())  # 2
```

**Explanation:**
Balances two heaps so that median can be extracted in O(1).

---

### 33. **Maximum Subarray Sum Using Divide and Conquer**

**Problem:**
Find maximum sum of a contiguous subarray.

**Solution:**

```python
def max_sub_array(nums):
    def helper(l, r):
        if l == r:
            return nums[l], nums[l], nums[l], nums[l]
        mid = (l + r) // 2
        left_sum, left_prefix, left_suffix, left_max = helper(l, mid)
        right_sum, right_prefix, right_suffix, right_max = helper(mid+1, r)

        total_sum = left_sum + right_sum
        prefix_sum = max(left_prefix, left_sum + right_prefix)
        suffix_sum = max(right_suffix, right_sum + left_suffix)
        max_sum = max(left_max, right_max, left_suffix + right_prefix)

        return total_sum, prefix_sum, suffix_sum, max_sum

    return helper(0, len(nums)-1)[3]

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(nums))  # Output: 6
```

**Explanation:**
Divide array into halves, calculate 4 values per half and combine results.

---

### 34. **Count Inversions**

**Problem:**
Count number of pairs `(i, j)` with `i < j` and `arr[i] > arr[j]`.

**Solution:**

```python
def count_inversions(arr):
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums, 0
        mid = len(nums) // 2
        left, left_inv = merge_sort(nums[:mid])
        right, right_inv = merge_sort(nums[mid:])
        merged = []
        i = j = inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        merged += left[i:]
        merged += right[j:]
        return merged, inv + left_inv + right_inv

    _, inv_count = merge_sort(arr)
    return inv_count

arr = [2, 4, 1, 3, 5]
print(count_inversions(arr))  # Output: 3
```

**Explanation:**
Uses merge sort and counts how many right elements jump over left elements.

---

### 35. **Skyline Problem**

**Problem:**
Given buildings represented by `(start, end, height)`, return the skyline formed by these buildings.

**Solution:**
Divide and conquer merges skylines of subsets.

```python
def get_skyline(buildings):
    def merge(left, right):
        h1 = h2 = 0
        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                x, h1 = left[i]
                i += 1
            else:
                x, h2 = right[j]
                j += 1
            max_h = max(h1, h2)
            if not result or result[-1][1] != max_h:
                result.append([x, max_h])
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def divide(buildings):
        if not buildings:
            return []
        if len(buildings) == 1:
            start, end, height = buildings[0]
            return [[start, height], [end, 0]]
        mid = len(buildings) // 2
        left = divide(buildings[:mid])
        right = divide(buildings[mid:])
        return merge(left, right)

    return divide(buildings)

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(get_skyline(buildings))
```

**Explanation:**
Divide buildings into halves, recursively find skylines, then merge.

---

These problems illustrate how divide and conquer methods, sometimes combined with binary search, heaps, or merge sort, solve complex problems efficiently.

If you want me to continue with more problems or explanations on a specific topic, just say!
