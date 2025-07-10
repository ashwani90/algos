Absolutely! Here are **10 intermediate-level prefix sum problems** with detailed explanations and Python solutions:

---

### 1. **Longest Subarray with Sum K**

**Problem:**
Given an array `nums` and an integer `k`, find the length of the longest subarray with sum exactly `k`.

**Explanation:**
Use prefix sums with a hashmap to store the earliest index for each prefix sum. When you find `prefix_sum - k` in the map, update max length.

```python
def longest_subarray_sum_k(nums, k):
    prefix_map = {0: -1}  # prefix sum to index
    prefix_sum = 0
    max_len = 0
    
    for i, num in enumerate(nums):
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    return max_len

# Example
print(longest_subarray_sum_k([1, -1, 5, -2, 3], 3))  # Output: 4
```

---

### 2. **Count Subarrays with Sum Divisible by K**

**Problem:**
Count the number of subarrays whose sum is divisible by `k`.

**Explanation:**
Use prefix sums mod `k`. If two prefix sums have the same remainder mod `k`, subarray between them is divisible by `k`.

```python
def subarrays_div_by_k(nums, k):
    prefix_map = {0: 1}
    prefix_sum = 0
    count = 0
    
    for num in nums:
        prefix_sum = (prefix_sum + num) % k
        count += prefix_map.get(prefix_sum, 0)
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    return count

# Example
print(subarrays_div_by_k([4,5,0,-2,-3,1], 5))  # Output: 7
```

---

### 3. **Number of Subarrays with Sum in Range**

**Problem:**
Count the number of subarrays whose sum lies between `lower` and `upper`.

**Explanation:**
Use prefix sums and a modified merge sort or a balanced tree. Here, a simpler solution with prefix sums and binary search is shown.

```python
from bisect import bisect_left, bisect_right

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

# Example
print(count_range_sum([-2,5,-1], -2, 2))  # Output: 3
```

---

### 4. **Maximum Size Subarray Sum Equals k**

**Problem:**
Find the maximum length of a subarray that sums to `k`.

**Explanation:**
Similar to problem 1, keep earliest prefix sums in a hashmap to find longest subarray length with sum k.

```python
def max_subarray_len(nums, k):
    prefix_map = {0: -1}
    prefix_sum = 0
    max_len = 0
    
    for i, num in enumerate(nums):
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    return max_len

# Example
print(max_subarray_len([1,-1,5,-2,3], 3))  # Output: 4
```

---

### 5. **Number of Ways to Split Array**

**Problem:**
Count the number of ways to split an array into 3 parts with equal sum.

**Explanation:**
Calculate total sum. If divisible by 3, track prefix sums to count valid splits.

```python
def ways_to_split(nums):
    total = sum(nums)
    if total % 3 != 0:
        return 0
    part_sum = total // 3
    prefix_sum = 0
    count = 0
    ways = 0
    
    for i in range(len(nums) - 1):
        prefix_sum += nums[i]
        if prefix_sum == 2 * part_sum:
            ways += count
        if prefix_sum == part_sum:
            count += 1
    return ways

# Example
print(ways_to_split([1,2,3,0,3]))  # Output: 2
```

---

### 6. **Maximum Subarray Sum Circular**

**Problem:**
Find maximum sum subarray in a circular array.

**Explanation:**
Use prefix sums to find max subarray sum normally, and also find minimum subarray sum to calculate max sum circularly.

```python
def max_subarray_sum_circular(nums):
    total = sum(nums)
    
    # Standard max subarray sum (Kadane's)
    max_sum = curr_max = nums[0]
    min_sum = curr_min = nums[0]
    
    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)
        curr_min = min(num, curr_min + num)
        min_sum = min(min_sum, curr_min)
        
    return max_sum if max_sum < 0 else max(max_sum, total - min_sum)

# Example
print(max_subarray_sum_circular([1,-2,3,-2]))  # Output: 3
```

---

### 7. **Longest Subarray with Equal Number of 0s and 1s**

**Problem:**
Find the longest contiguous subarray containing equal number of 0s and 1s.

**Explanation:**
Convert 0 to -1, then find longest subarray with sum 0 using prefix sums and hashmap.

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

# Example
print(find_max_length([0,1,0,1,0,1,1]))  # Output: 6
```

---

### 8. **Maximum Number of Vowels in a Substring of Given Length**

**Problem:**
Given a string and an integer k, find max number of vowels in any substring of length k.

**Explanation:**
Use prefix sums to count vowels and sliding window for max.

```python
def max_vowels(s, k):
    vowels = set('aeiou')
    prefix = [0]
    for char in s:
        prefix.append(prefix[-1] + (1 if char in vowels else 0))
    max_v = 0
    for i in range(k, len(prefix)):
        max_v = max(max_v, prefix[i] - prefix[i-k])
    return max_v

# Example
print(max_vowels("abciiidef", 3))  # Output: 3
```

---

### 9. **Count Number of Nice Subarrays**

**Problem:**
Count subarrays with exactly `k` odd numbers.

**Explanation:**
Use prefix sums of counts of odd numbers and hashmap.

```python
def number_of_subarrays(nums, k):
    count_map = {0: 1}
    prefix_odd_count = 0
    result = 0
    
    for num in nums:
        prefix_odd_count += num % 2
        result += count_map.get(prefix_odd_count - k, 0)
        count_map[prefix_odd_count] = count_map.get(prefix_odd_count, 0) + 1
    return result

# Example
print(number_of_subarrays([1,1,2,1,1], 3))  # Output: 2
```

---

### 10. **Minimum Size Subarray Sum**

**Problem:**
Find the minimal length of a contiguous subarray of which the sum ≥ `s`.

**Explanation:**
Use prefix sums with binary search to find minimal subarray length.

```python
from bisect import bisect_left

def min_subarray_len(s, nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    min_len = float('inf')
    for i in range(1, len(prefix)):
        target = prefix[i] - s
        bound = bisect_left(prefix, target)
        if bound < i:
            min_len = min(min_len, i - bound)
    return 0 if min_len == float('inf') else min_len

# Example
print(min_subarray_len(7, [2,3,1,2,4,3]))  # Output: 2
```

---

If you'd like me to explain any specific problem more or provide variations, just let me know!
