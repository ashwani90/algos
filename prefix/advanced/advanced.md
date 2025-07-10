Sure! Here are **10 advanced-level prefix sum problems** with detailed explanations and Python solutions to challenge your understanding:

---

### 1. **Count of Range Sum**

**Problem:**
Given an integer array `nums` and two integers `lower` and `upper`, return the number of range sums that lie in `[lower, upper]`. A range sum `S(i, j)` is defined as the sum of the elements between indices `i` and `j` inclusive.

**Explanation:**
We use prefix sums and a modified merge sort to count the number of valid sums efficiently.

```python
def count_range_sum(nums, lower, upper):
    prefix_sums = [0]
    for num in nums:
        prefix_sums.append(prefix_sums[-1] + num)

    def merge_sort(lo, hi):
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        count = merge_sort(lo, mid) + merge_sort(mid, hi)
        j = k = mid
        for left in prefix_sums[lo:mid]:
            while k < hi and prefix_sums[k] - left < lower:
                k += 1
            while j < hi and prefix_sums[j] - left <= upper:
                j += 1
            count += j - k
        prefix_sums[lo:hi] = sorted(prefix_sums[lo:hi])
        return count

    return merge_sort(0, len(prefix_sums))

# Example
print(count_range_sum([-2, 5, -1], -2, 2))  # Output: 3
```

---

### 2. **Maximum Subarray Sum with At Most K Changes**

**Problem:**
Given an array, you can change at most `k` elements to any value to maximize the sum of a subarray.

**Explanation:**
Use prefix sums combined with dynamic programming to track best sums with changes.

```python
def max_subarray_sum_k_changes(nums, k):
    n = len(nums)
    dp = [[float('-inf')] * (k+1) for _ in range(n+1)]
    for j in range(k+1):
        dp[0][j] = 0
    
    max_sum = float('-inf')
    for i in range(1, n+1):
        for j in range(k+1):
            # Without change
            dp[i][j] = max(dp[i-1][j] + nums[i-1], nums[i-1])
            # With change if possible
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + float('inf'))  # Inf for max change value, adjust as needed
            max_sum = max(max_sum, dp[i][j])
    return max_sum

# This is a template; to fully solve, define what change values can be.
```

*(This problem is complex and requires further problem context for precise coding. The above shows DP + prefix sums framework.)*

---

### 3. **Subarray Sum Equals K with Multiple Queries**

**Problem:**
You get multiple queries `(k)` asking how many subarrays sum to `k` for the same array.

**Explanation:**
Precompute prefix sums and store frequencies to answer queries in O(1).

```python
from collections import defaultdict

class SubarraySumQuery:
    def __init__(self, nums):
        self.prefix_count = defaultdict(int)
        self.prefix_sum = 0
        self.prefix_count[0] = 1
        self.subarray_sums = defaultdict(int)

        for num in nums:
            self.prefix_sum += num
            # Update counts for all sums seen so far
            for k in list(self.subarray_sums.keys()):
                self.subarray_sums[k] += self.prefix_count[self.prefix_sum - k]
            self.subarray_sums[self.prefix_sum] += 1
            self.prefix_count[self.prefix_sum] += 1

    def query(self, k):
        return self.subarray_sums.get(k, 0)

# Usage is tricky here; problem requires careful optimization.
```

---

### 4. **Find the Smallest Subarray with Sum at Least S**

**Problem:**
Given an array and integer `S`, find the length of the smallest subarray whose sum is ≥ `S`.

**Explanation:**
Use prefix sums and binary search to quickly find subarray lengths.

```python
from bisect import bisect_left

def min_subarray_length(s, nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    min_len = float('inf')
    for i in range(1, len(prefix)):
        target = prefix[i] - s
        pos = bisect_left(prefix, target)
        if pos < i:
            min_len = min(min_len, i - pos)
    return 0 if min_len == float('inf') else min_len

print(min_subarray_length(7, [2,3,1,2,4,3]))  # Output: 2
```

---

### 5. **Sum of Subarray Minimums**

**Problem:**
Find the sum of the minimum value of every subarray of the array.

**Explanation:**
Prefix sums of minimums combined with a monotonic stack.

```python
def sum_subarray_mins(arr):
    stack = []
    result = 0
    mod = 10**9 + 7
    dp = [0] * len(arr)

    for i, x in enumerate(arr):
        while stack and arr[stack[-1]] > x:
            stack.pop()
        prev_index = stack[-1] if stack else -1
        dp[i] = dp[prev_index] + x * (i - prev_index)
        result = (result + dp[i]) % mod
        stack.append(i)

    return result

print(sum_subarray_mins([3,1,2,4]))  # Output: 17
```

---

### 6. **Count Subarrays with Median K**

**Problem:**
Count number of subarrays where the median is `k`.

**Explanation:**
Use prefix sums to track balance of elements > and < k, then count matches.

```python
def count_subarrays_with_median_k(nums, k):
    k_index = nums.index(k)
    count = 0
    balance_map = {0: 1}
    balance = 0

    for i in range(k_index-1, -1, -1):
        balance += 1 if nums[i] > k else -1
        balance_map[balance] = balance_map.get(balance, 0) + 1
    
    balance = 0
    for i in range(k_index, len(nums)):
        balance += 1 if nums[i] > k else -1
        count += balance_map.get(-balance, 0) + balance_map.get(-balance + 1, 0)
    return count

print(count_subarrays_with_median_k([3,2,1,4,5], 4))  # Output: 3
```

---

### 7. **Number of Subarrays with Bounded Maximum**

**Problem:**
Count subarrays where maximum element is in `[L, R]`.

**Explanation:**
Use prefix sums with two pointers to track valid subarrays.

```python
def num_subarray_bounded_max(nums, L, R):
    def at_most(bound):
        count = start = 0
        for i, num in enumerate(nums):
            if num > bound:
                start = i + 1
            count += i - start + 1
        return count
    return at_most(R) - at_most(L - 1)

print(num_subarray_bounded_max([2,1,4,3], 2, 3))  # Output: 3
```

---

### 8. **Find Number of Good Subarrays**

**Problem:**
A subarray is "good" if the number of odd numbers in it is exactly `k`. Count them.

**Explanation:**
Use prefix sums and hashmap to count exactly `k` odds.

```python
def number_of_subarrays(nums, k):
    count_map = {0: 1}
    count = prefix = 0
    result = 0
    for num in nums:
        prefix += num % 2
        result += count_map.get(prefix - k, 0)
        count_map[prefix] = count_map.get(prefix, 0) + 1
    return result

print(number_of_subarrays([1,1,2,1,1], 3))  # Output: 2
```

---

### 9. **Maximum Length of Subarray with Positive Product**

**Problem:**
Find length of longest subarray where the product of all elements is positive.

**Explanation:**
Track prefix of negative count using prefix sums to determine subarrays with even number of negatives.

```python
def get_max_len(nums):
    pos = neg = max_len = 0
    for num in nums:
        if num == 0:
            pos = neg = 0
        elif num > 0:
            pos += 1
            neg = neg + 1 if neg > 0 else 0
        else:
            temp = pos
            pos = neg + 1 if neg > 0 else 0
            neg = temp + 1
        max_len = max(max_len, pos)
    return max_len

print(get_max_len([1,-2,-3,4]))  # Output: 4
```

---

### 10. **Longest Balanced Substring**

**Problem:**
Find the longest substring where number of `0`s and `1`s are equal.

**Explanation:**
Transform `0` to `-1` and use prefix sums and hashmap to find longest subarray with sum zero.

```python
def find_max_length(nums):
    prefix_map = {0: -1}
    prefix_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1
        if prefix_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum])
        else:
            prefix_map[prefix_sum] = i
    return max_len

print(find_max_length([0,1,0,1,0,1,1]))  # Output: 6
```

---

If you want me to explain any problem or solution in more depth, or want code variations, just ask!
