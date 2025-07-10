Sure! Here are **10 merge sort problems** along with detailed solutions and explanations. Merge sort is a classic divide-and-conquer sorting algorithm that splits the array, sorts subarrays recursively, and merges them back.

---

### 1. Basic Merge Sort Implementation

**Problem:**
Implement merge sort to sort an array in ascending order.

**Solution:**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
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

arr = [5,3,8,6,2,7,1,4]
print(merge_sort(arr))  # Output: [1,2,3,4,5,6,7,8]
```

**Explanation:**
Split array into halves recursively. Merge two sorted halves in linear time.

---

### 2. Count Inversions in an Array

**Problem:**
Count the number of inversions in an array — pairs `(i, j)` such that `i < j` and `arr[i] > arr[j]`.

**Solution:**

```python
def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr)//2
    left, left_inv = merge_sort_count(arr[:mid])
    right, right_inv = merge_sort_count(arr[mid:])
    merged, merge_inv = merge_count(left, right)
    return merged, left_inv + right_inv + merge_inv

def merge_count(left, right):
    result = []
    i = j = inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv_count += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv_count

arr = [2,4,1,3,5]
sorted_arr, inversions = merge_sort_count(arr)
print(inversions)  # Output: 3
```

**Explanation:**
While merging, when an element from right subarray goes before left, it contributes to inversions equal to remaining left elements.

---

### 3. Merge K Sorted Lists

**Problem:**
Given `k` sorted linked lists, merge them into one sorted list.

**Solution (using divide and conquer with merge sort idea):**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

def merge_k_lists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists)//2
    left = merge_k_lists(lists[:mid])
    right = merge_k_lists(lists[mid:])
    return merge_two_lists(left, right)
```

**Explanation:**
Divide `k` lists into halves recursively, merge pairs of sorted lists, like merge sort merges arrays.

---

### 4. Sort an Array of 0s, 1s and 2s Using Merge Sort

**Problem:**
Sort an array consisting of only 0s, 1s, and 2s.

**Solution:**

```python
def merge_sort_012(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort_012(arr[:mid])
    right = merge_sort_012(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [0,2,1,0,2,1,0]
print(merge_sort_012(arr))  # Output: [0,0,0,1,1,2,2]
```

**Explanation:**
Same as normal merge sort; elements are limited but approach is identical.

---

### 5. Find the Majority Element (Appears more than n/2 times)

**Problem:**
Find the majority element using merge sort.

**Solution:**

```python
def merge_sort_majority(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort_majority(arr[:mid])
    right = merge_sort_majority(arr[mid:])
    merged = merge(left, right)
    return merged

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def majority_element(arr):
    sorted_arr = merge_sort_majority(arr)
    count = 1
    candidate = sorted_arr[0]
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == candidate:
            count += 1
        else:
            count = 1
            candidate = sorted_arr[i]
        if count > len(arr)//2:
            return candidate
    return candidate

arr = [2,2,1,1,1,2,2]
print(majority_element(arr))  # Output: 2
```

**Explanation:**
Sorting brings identical elements together, so the majority element will be in the middle of the sorted array.

---

### 6. Count Smaller Numbers After Self (Hard)

**Problem:**
For each element in the array, count how many smaller elements appear to the right.

**Solution (using merge sort counting):**

```python
def count_smaller(nums):
    res = [0] * len(nums)
    enum = list(enumerate(nums))

    def merge_sort(arr):
        mid = len(arr)//2
        if mid:
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            i = j = 0
            merged = []
            while i < len(left) or j < len(right):
                if j == len(right) or (i < len(left) and left[i][1] <= right[j][1]):
                    res[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            return merged
        else:
            return arr

    merge_sort(enum)
    return res

print(count_smaller([5,2,6,1]))  # Output: [2,1,1,0]
```

**Explanation:**
While merging, count how many elements from the right array move before elements from the left array.

---

### 7. Sort Linked List

**Problem:**
Sort a singly linked list in O(n log n) time and constant space.

**Solution:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_list(head):
    if not head or not head.next:
        return head

    # Split list in half
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None

    left = sort_list(head)
    right = sort_list(mid)
    return merge(left, right)

def merge(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

**Explanation:**
We split the list into halves, sort each half recursively, then merge them.

---

### 8. Maximum Number of Non-overlapping Intervals (Greedy + Sort)

**Problem:**
Given intervals, select max number of non-overlapping intervals.

**Solution (sort intervals by end time using merge sort):**

```python
def merge_sort_intervals(intervals):
    if len(intervals) <= 1:
        return intervals
    mid = len(intervals)//2
    left = merge_sort_intervals(intervals[:mid])
    right = merge_sort_intervals(intervals[mid:])
```


Continuing from problem 8 — **Maximum Number of Non-overlapping Intervals** — here is the full solution and explanation, then problems 9 and 10.

---

### 8. Maximum Number of Non-overlapping Intervals

**Problem:**
Given a list of intervals `[start, end]`, find the maximum number of intervals that don't overlap.

**Solution:**

```python
def merge_sort_intervals(intervals):
    if len(intervals) <= 1:
        return intervals
    mid = len(intervals)//2
    left = merge_sort_intervals(intervals[:mid])
    right = merge_sort_intervals(intervals[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Sort by end time
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def max_non_overlapping_intervals(intervals):
    sorted_intervals = merge_sort_intervals(intervals)
    count = 0
    end = float('-inf')

    for interval in sorted_intervals:
        if interval[0] >= end:
            count += 1
            end = interval[1]
    return count

intervals = [[1,3],[2,4],[3,5],[7,8]]
print(max_non_overlapping_intervals(intervals))  # Output: 3
```

**Explanation:**
Sort intervals by their end times to greedily select the earliest finishing intervals first, allowing maximum non-overlapping intervals.

---

### 9. Find the kth Smallest Element in an Unsorted Array

**Problem:**
Find the kth smallest element using a merge sort based approach.

**Solution:**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
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

def kth_smallest(arr, k):
    sorted_arr = merge_sort(arr)
    return sorted_arr[k-1] if 0 < k <= len(arr) else None

arr = [7,10,4,3,20,15]
print(kth_smallest(arr, 3))  # Output: 7
```

**Explanation:**
Sort array using merge sort and then return the element at index `k-1`.

---

### 10. Find Intersection of Two Sorted Arrays

**Problem:**
Find the intersection of two sorted arrays (elements common to both).

**Solution:**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] == right[j]:
            result.append(left[i])
            i += 1
            j += 1
        elif left[i] < right[j]:
            i += 1
        else:
            j += 1
    return result

def intersection(arr1, arr2):
    sorted_arr1 = merge_sort(arr1)
    sorted_arr2 = merge_sort(arr2)
    return merge(sorted_arr1, sorted_arr2)

arr1 = [1,3,4,5,7]
arr2 = [2,3,5,6]
print(intersection(arr1, arr2))  # Output: [3,5]
```

**Explanation:**
Sort both arrays with merge sort, then use two pointers to find common elements.

---

If you want me to continue with more problems or explore any of these in more depth, just say!
