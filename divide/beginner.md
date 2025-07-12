Certainly! Here are **10 beginner-level divide and conquer problems** along with their solutions and detailed explanations in Python.

---

### 1. **Merge Sort**

**Problem:**
Sort an array using the divide and conquer approach.

**Solution:**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([5, 3, 8, 6, 2, 7, 4, 1]))
```

**Explanation:**
The array is recursively divided into halves until single elements are left (base case). Then merge the sorted halves by comparing elements from both subarrays. The divide step splits, conquer step sorts recursively, and combine step merges.

---

### 2. **Binary Search**

**Problem:**
Search for an element in a sorted array.

**Solution:**

```python
def binary_search(arr, target):
    def helper(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, high)
        else:
            return helper(low, mid - 1)
    return helper(0, len(arr) - 1)

print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3
```

**Explanation:**
Divide the search range in half at each step, checking the middle element and continuing on the left or right subarray recursively.

---

### 3. **Find Maximum Element**

**Problem:**
Find the maximum element in an array using divide and conquer.

**Solution:**

```python
def find_max(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)
    return max(left_max, right_max)

arr = [2, 10, 5, 8, 1]
print(find_max(arr, 0, len(arr) - 1))  # Output: 10
```

**Explanation:**
Divide the array into halves, find the maximum in each half, then combine by taking the max of the two.

---

### 4. **Count Inversions in an Array**

**Problem:**
Count how many pairs `(i, j)` exist such that `i < j` and `arr[i] > arr[j]`.

**Solution:**

```python
def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, left_inv = merge_sort(arr[:mid])
        right, right_inv = merge_sort(arr[mid:])
        merged, split_inv = merge(left, right)
        return merged, left_inv + right_inv + split_inv

    def merge(left, right):
        i = j = inv = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i  # Count inversions
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    _, count = merge_sort(arr)
    return count

print(count_inversions([2, 4, 1, 3, 5]))  # Output: 3
```

**Explanation:**
Use merge sort to count inversions during merge when elements from the right array come before those from the left array.

---

### 5. **Find the k-th Smallest Element**

**Problem:**
Find the k-th smallest element in an unsorted array using a divide and conquer approach (Quickselect).

**Solution:**

```python
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[len(arr) // 2]
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

print(quickselect([7, 10, 4, 3, 20, 15], 3))  # Output: 7 (0-indexed)
```

**Explanation:**
Select a pivot, partition array into smaller and larger elements, recursively select in the partition containing the k-th smallest element.

---

### 6. **Power Function (Exponentiation by Squaring)**

**Problem:**
Compute `x^n` efficiently using divide and conquer.

**Solution:**

```python
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

print(power(2, 10))  # Output: 1024
```

**Explanation:**
Split the power `n` into halves recursively, multiply halves and the extra `x` if `n` is odd.

---

### 7. **Find Majority Element**

**Problem:**
Find element that appears more than n/2 times in array (if exists) using divide and conquer.

**Solution:**

```python
def majority_element(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left = majority_element(arr, low, mid)
    right = majority_element(arr, mid + 1, high)
    if left == right:
        return left
    
    left_count = sum(1 for i in range(low, high+1) if arr[i] == left)
    right_count = sum(1 for i in range(low, high+1) if arr[i] == right)
    return left if left_count > right_count else right

arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(arr, 0, len(arr) - 1))  # Output: 2
```

**Explanation:**
Divide array, find majority in left and right. If they differ, count occurrences to determine majority.

---

### 8. **Closest Pair of Points**

**Problem:**
Given points on a plane, find the pair with the minimum distance between them.

**Solution:**

```python
import math

def closest_pair(points):
    def dist(p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def helper(points_sorted_x, points_sorted_y):
        if len(points_sorted_x) <= 3:
            min_d = float('inf')
            for i in range(len(points_sorted_x)):
                for j in range(i+1, len(points_sorted_x)):
                    min_d = min(min_d, dist(points_sorted_x[i], points_sorted_x[j]))
            return min_d

        mid = len(points_sorted_x) // 2
        mid_x = points_sorted_x[mid][0]
        left_x = points_sorted_x[:mid]
        right_x = points_sorted_x[mid:]

        left_y = list(filter(lambda p: p[0] <= mid_x, points_sorted_y))
        right_y = list(filter(lambda p: p[0] > mid_x, points_sorted_y))

        d_left = helper(left_x, left_y)
        d_right = helper(right_x, right_y)
        d = min(d_left, d_right)

        strip = [p for p in points_sorted_y if abs(p[0] - mid_x) < d]

        for i in range(len(strip)):
            for j in range(i+1, min(i+7, len(strip))):
                d = min(d, dist(strip[i], strip[j]))

        return d

    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])
    return helper(points_sorted_x, points_sorted_y)

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(points))  # Output: 1.4142...
```

**Explanation:**
Divide points into two halves, find minimum distance in each half, then check points near dividing line in sorted order to find closer pairs.

---

### 9. **Sum of Array Elements**

**Problem:**
Sum all elements of an array using divide and

Certainly! Continuing with problem #9 and #10:

---

### 9. **Sum of Array Elements Using Divide and Conquer**

**Problem:**
Find the sum of all elements in an array using divide and conquer.

**Solution:**

```python
def array_sum(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_sum = array_sum(arr, low, mid)
    right_sum = array_sum(arr, mid + 1, high)
    return left_sum + right_sum

arr = [1, 2, 3, 4, 5]
print(array_sum(arr, 0, len(arr) - 1))  # Output: 15
```

**Explanation:**
The array is divided into two halves recursively. The sum of the left half and the right half is computed separately and then combined.

---

### 10. **Count Number of Occurrences of a Number in Sorted Array**

**Problem:**
Count how many times a given number appears in a sorted array using divide and conquer.

**Solution:**

```python
def count_occurrences(arr, target):
    def find_left(arr, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if (mid == 0 or arr[mid-1] < target) and arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return find_left(arr, target, mid + 1, high)
        else:
            return find_left(arr, target, low, mid - 1)

    def find_right(arr, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if (mid == len(arr) - 1 or arr[mid+1] > target) and arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return find_right(arr, target, low, mid - 1)
        else:
            return find_right(arr, target, mid + 1, high)

    left_index = find_left(arr, target, 0, len(arr) - 1)
    if left_index == -1:
        return 0
    right_index = find_right(arr, target, 0, len(arr) - 1)
    return right_index - left_index + 1

arr = [1, 2, 2, 2, 3, 4, 5]
print(count_occurrences(arr, 2))  # Output: 3
```

**Explanation:**
Find the leftmost and rightmost positions of the target element using binary search (divide and conquer). The difference plus one gives the count of occurrences.

---

If you'd like, I can also provide problems with increasing difficulty or on other topics! Would you like me to continue?


Sure! Here are 10 more **divide and conquer** problems with their solutions and explanations:

---

### 11. **Find the Maximum Element in an Array**

**Problem:**
Find the maximum element in an array using divide and conquer.

**Solution:**

```python
def find_max(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)
    return max(left_max, right_max)

arr = [2, 8, 1, 5, 3]
print(find_max(arr, 0, len(arr) - 1))  # Output: 8
```

**Explanation:**
Divide the array into two halves, recursively find the maximum in each half, then return the overall maximum.

---

### 12. **Find the Minimum Element in an Array**

**Problem:**
Find the minimum element in an array using divide and conquer.

**Solution:**

```python
def find_min(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_min = find_min(arr, low, mid)
    right_min = find_min(arr, mid + 1, high)
    return min(left_min, right_min)

arr = [9, 2, 6, 4, 1]
print(find_min(arr, 0, len(arr) - 1))  # Output: 1
```

**Explanation:**
Similar to maximum, split the array and find the minimum of each half, then pick the smallest overall.

---

### 13. **Count Inversions in an Array**

**Problem:**
Count how many pairs `(i, j)` exist such that `i < j` and `arr[i] > arr[j]`.

**Solution:**

```python
def merge(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
            k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for idx in range(left, right + 1):
        arr[idx] = temp[idx]

    return inv_count

def merge_sort(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid, right)
    return inv_count

arr = [2, 4, 1, 3, 5]
temp = [0]*len(arr)
print(merge_sort(arr, temp, 0, len(arr) - 1))  # Output: 3
```

**Explanation:**
This is a classic inversion count problem solved via modified merge sort. When merging two sorted halves, every time an element from the right half precedes one from the left, it contributes to the inversion count.

---

### 14. **Find Majority Element (More than n/2 times)**

**Problem:**
Find the element that appears more than n/2 times in the array using divide and conquer.

**Solution:**

```python
def majority_element(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2
    left = majority_element(arr, low, mid)
    right = majority_element(arr, mid + 1, high)

    if left == right:
        return left

    left_count = sum(1 for i in range(low, high + 1) if arr[i] == left)
    right_count = sum(1 for i in range(low, high + 1) if arr[i] == right)

    return left if left_count > right_count else right

arr = [2, 2, 1, 1, 2]
print(majority_element(arr, 0, len(arr) - 1))  # Output: 2
```

**Explanation:**
Divide the array into halves, find the majority element in each half, then combine results by counting occurrences in the current range.

---

### 15. **Closest Pair of Points**

**Problem:**
Given points on a plane, find the pair with the smallest distance.

**Solution:**
This is a classic geometry divide and conquer problem, too large to write fully here, but key steps are:

* Sort points by x-coordinate
* Divide points into two halves
* Recursively find closest pair in each half
* Check points near the dividing line for cross-boundary closest pairs

**Explanation:**
Divide and conquer reduces the problem from O(n²) to O(n log n).

---

### 16. **Maximum Subarray Sum (Divide and Conquer)**

**Problem:**
Find the maximum sum of a contiguous subarray using divide and conquer.

**Solution:**

```python
def max_crossing_sum(arr, low, mid, high):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total

    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, high + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total

    return left_sum + right_sum

def max_subarray_sum(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2
    left_max = max_subarray_sum(arr, low, mid)
    right_max = max_subarray_sum(arr, mid + 1, high)
    cross_max = max_crossing_sum(arr, low, mid, high)

    return max(left_max, right_max, cross_max)

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(arr, 0, len(arr) - 1))  # Output: 6
```

**Explanation:**
Find max subarray sum in left half, right half, and crossing mid, and pick the max.

---

### 17. **Find kth Smallest Element in an Array**

**Problem:**
Find kth smallest element using divide and conquer (QuickSelect).

**Solution:**

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def kth_smallest(arr, low, high, k):
    if low <= high:
        pi = partition(arr, low, high)
        if pi == k - 1:
            return arr[pi]
        elif pi > k - 1:
            return kth_smallest(arr, low, pi - 1, k)
        else:
            return kth_smallest(arr, pi + 1, high, k)
    return None

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(arr, 0, len(arr) - 1, k))  # Output: 7
```

**Explanation:**
QuickSelect partitions the array like quicksort, but only recurses into the part containing the kth element.

---

### 18. **Count Number of Elements Smaller Than or Equal to X**

**Problem:**
Given a sorted array, count how many elements are ≤ X using divide and conquer (binary search).

**Solution:**

```python
def count_smaller_equal(arr, x):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result + 1 if result != -1 else 0

arr = [1, 2, 4, 4, 5, 6]
x = 4
print(count_smaller_equal(arr, x))  # Output: 4
```

**Explanation:**
Use binary search to find the rightmost index of element ≤ x, count is index + 1.

---

### 19. **Multiply Two Large Numbers Using Divide and Conquer (Karatsuba)**

**Problem:**
Multiply two large numbers represented as strings efficiently.

**Solution:**
Due to complexity, here's the key idea:

* Split numbers into halves
* Recursively multiply parts
* Combine using Karatsuba’s formula to reduce multiplications

```python
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    a = x // 10**half
    b = x % 10**half
    c = y // 10**half
    d = y % 10**half

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(a + b, c + d)

    return ac * 10**(2*half) + (ab_cd - ac - bd) * 10**half + bd

print(karatsuba(1234, 5678))  # Output: 7006652
```

**Explanation:**
Karatsuba reduces multiplication complexity from O(n²) to approximately O(n^1.585).

---

### 20. **Count Number of Occurrences of a Target in a Sorted Array (Binary Search)**

**Problem:**
Given a sorted array, count how many times a target appears.

**Solution:** (Similar to problem 10 but iterative)

```python
def count_occurrences(arr, target):
    def binary_search_left():
        low, high = 0, len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def binary_search_right():
        low, high = 0, len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    left = binary_search_left()
    if left == -1:
        return 0
    right = binary_search_right()
    return right - left + 1

arr = [1, 2, 2, 2, 3, 4]
print(count_occurrences(arr, 2))  # Output: 3
```

**Explanation:**
Find leftmost and rightmost indices of target with binary search and calculate count.

---

Let me know if you want me to keep going or switch topics!
