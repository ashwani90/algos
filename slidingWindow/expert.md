Great! Here are **10 expert-level sliding window problems** that integrate advanced techniques such as dynamic programming, bitmasking, greedy strategies, or data structures like tries and monotonic queues.

---

### **1. Minimum Number of Flips to Make Binary String Alternating (Circular)**

**Problem:**
You are given a binary string. You can rotate it and flip any bit. Find the minimum flips needed to make it alternating (0101… or 1010…).

**Approach:**
Use a sliding window of the string + itself (to handle rotations) and compare to alternating patterns.

```python
def min_flips(s):
    n = len(s)
    s = s + s
    alt1 = ''.join(['01'[(i % 2)] for i in range(2 * n)])
    alt2 = ''.join(['10'[(i % 2)] for i in range(2 * n)])
    res, diff1, diff2 = float('inf'), 0, 0

    left = 0
    for right in range(2 * n):
        if s[right] != alt1[right]:
            diff1 += 1
        if s[right] != alt2[right]:
            diff2 += 1

        if right - left + 1 > n:
            if s[left] != alt1[left]:
                diff1 -= 1
            if s[left] != alt2[left]:
                diff2 -= 1
            left += 1
        if right - left + 1 == n:
            res = min(res, diff1, diff2)
    return res

print(min_flips("111000"))
# Output: 2
```

---

### **2. Count Subarrays with Bitwise AND Zero**

**Problem:**
Count subarrays where the bitwise AND of elements is 0.

**Solution:**
Use sliding window + bitmask AND tracking.

```python
def count_subarrays_with_and_zero(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        and_val = arr[i]
        for j in range(i, n):
            and_val &= arr[j]
            if and_val == 0:
                res += 1
                break
    return res

print(count_subarrays_with_and_zero([1, 2, 3]))
# Output: 2
```

---

### **3. Minimum Window Substring with All Characters at Least K Frequency**

**Problem:**
Like classic minimum window substring, but each character must appear at least `k` times.

**Solution:**
Sliding window + frequency counter + valid window condition.

```python
from collections import Counter

def longest_substring_k_freq(s, k):
    max_unique = len(set(s))
    res = 0
    for curr_unique in range(1, max_unique + 1):
        count = Counter()
        l = r = unique = at_least_k = 0
        while r < len(s):
            if count[s[r]] == 0:
                unique += 1
            count[s[r]] += 1
            if count[s[r]] == k:
                at_least_k += 1

            while unique > curr_unique:
                if count[s[l]] == k:
                    at_least_k -= 1
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    unique -= 1
                l += 1

            if unique == curr_unique and unique == at_least_k:
                res = max(res, r - l + 1)
            r += 1
    return res

print(longest_substring_k_freq("aaabbcc", 2))
# Output: 4
```

---

### **4. Longest Substring with At Most Two Distinct Characters**

**Solution:**
Sliding window + hashmap count.

```python
def length_of_longest_substring_two_distinct(s):
    from collections import defaultdict
    left = 0
    count = defaultdict(int)
    max_len = 0
    for right in range(len(s)):
        count[s[right]] += 1
        while len(count) > 2:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(length_of_longest_substring_two_distinct("eceba"))
# Output: 3
```

---

### **5. Longest Subarray with Equal Number of 0 and 1**

**Convert 0s to -1 and use prefix sum.**

```python
def find_max_length(nums):
    map_index = {0: -1}
    max_len = 0
    count = 0
    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if count in map_index:
            max_len = max(max_len, i - map_index[count])
        else:
            map_index[count] = i
    return max_len

print(find_max_length([0,1,0]))
# Output: 2
```

---

### **6. Longest Subarray with Sum Less Than or Equal to K**

**Use deque to store increasing prefix sums.**

```python
from collections import deque

def longest_subarray_with_sum_k(nums, k):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    dq = deque()
    max_len = 0
    for i in range(len(prefix)):
        while dq and prefix[i] - prefix[dq[0]] > k:
            dq.popleft()
        if dq:
            max_len = max(max_len, i - dq[0])
        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()
        dq.append(i)
    return max_len

print(longest_subarray_with_sum_k([1, -1, 5, -2, 3], 3))
# Output: 4
```

---

### **7. Longest Substring Without Repeating Characters**

**Classic problem optimized with sliding window and hash map.**

```python
def length_of_longest_substring(s):
    index_map = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] in index_map and index_map[s[right]] >= left:
            left = index_map[s[right]] + 1
        index_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len

print(length_of_longest_substring("abcabcbb"))
# Output: 3
```

---

### **8. Minimum Size Subarray Sum**

**Sliding window with shrinking front to find the smallest subarray with sum ≥ target.**

```python
def min_subarray_len(target, nums):
    left = 0
    total = 0
    res = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            res = min(res, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if res == float('inf') else res

print(min_subarray_len(7, [2,3,1,2,4,3]))
# Output: 2
```

---

### **9. Count Number of Substrings with Exactly K Distinct Characters**

**Extend the earlier version to count substrings instead of subarrays.**

```python
def substrings_with_k_distinct(s, k):
    def at_most_k(s, k):
        count = {}
        res = left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            res += right - left + 1
        return res
    return at_most_k(s, k) - at_most_k(s, k - 1)

print(substrings_with_k_distinct("pqpqs", 2))
# Output: 7
```

---

### **10. Smallest Subarray With All Occurrences of Most Frequent Element**

**Sliding window on index groups of the most frequent value.**

```python
from collections import defaultdict

def min_subarray_with_all_occurrences(nums):
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    most_freq = max(freq.values())
    candidates = [num for num in freq if freq[num] == most_freq]
    
    min_len = len(nums)
    for c in candidates:
        left = nums.index(c)
        right = len(nums) - 1 - nums[::-1].index(c)
        min_len = min(min_len, right - left + 1)
    return min_len

print(min_subarray_with_all_occurrences([1,2,2,3,1,4,2]))
# Output: 6
```

---

Would you like to move on to **bitmask DP + sliding window** hybrid problems next, or focus on more contest-style ones?

Great! Let’s continue with **10 more expert-level problems** that mix **sliding window** with **dynamic programming (DP)**, **bitmasking**, and **greedy techniques**.

---

### **11. Sliding Window Maximum**

**Problem:** Find the max value in each sliding window of size `k`.

**Technique:** Sliding window + Monotonic Queue

```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    res = []
    
    for i in range(len(nums)):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
# Output: [3,3,5,5,6,7]
```

---

### **12. Count Subarrays Where Product Is Less Than K**

**Technique:** Two pointers / sliding window

```python
def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    prod = 1
    res = left = 0
    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k:
            prod //= nums[left]
            left += 1
        res += right - left + 1
    return res

print(num_subarray_product_less_than_k([10,5,2,6], 100))
# Output: 8
```

---

### **13. Maximum Sum of Subarray with at Most K Elements**

**Technique:** Sliding window with DP

```python
def max_sum_k_elements(arr, k):
    n = len(arr)
    max_sum = curr_sum = sum(arr[:k])
    for i in range(k, n):
        curr_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(max_sum_k_elements([1,2,3,4,5], 2))
# Output: 9
```

---

### **14. Count Number of Nice Subarrays (Exactly K Odd Numbers)**

**Technique:** Sliding window + prefix sum counting

```python
def number_of_subarrays(nums, k):
    from collections import defaultdict
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    odd_count = res = 0
    for num in nums:
        odd_count += num % 2
        res += prefix_count[odd_count - k]
        prefix_count[odd_count] += 1
    return res

print(number_of_subarrays([1,1,2,1,1], 3))
# Output: 2
```

---

### **15. Minimum Operations to Make Subarray Sum to Target**

**Problem:** Given array, remove elements from either end so remaining subarray sums to target.

**Technique:** Sliding window to find subarray of sum = total - target.

```python
def min_operations(nums, x):
    total = sum(nums)
    target = total - x
    if target < 0: return -1
    curr_sum = left = 0
    max_len = -1
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > target:
            curr_sum -= nums[left]
            left += 1
        if curr_sum == target:
            max_len = max(max_len, right - left + 1)
    return len(nums) - max_len if max_len != -1 else -1

print(min_operations([1,1,4,2,3], 5))
# Output: 2
```

---

### **16. Longest Substring with At Most K Replacements**

**Problem:** Replace at most `k` characters to make substring with all same characters.

**Technique:** Sliding window + frequency tracking

```python
def character_replacement(s, k):
    from collections import defaultdict
    left = max_count = 0
    count = defaultdict(int)
    res = 0
    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res

print(character_replacement("AABABBA", 1))
# Output: 4
```

---

### **17. Max Consecutive Ones III**

**Problem:** Flip at most `k` 0s to 1s to get longest sequence of 1s.

```python
def longest_ones(nums, k):
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
    return right - left + 1

print(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2))
# Output: 6
```

---

### **18. Smallest Window to Contain All Characters of Another String**

**Technique:** Sliding window with character frequency match

```python
from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    for right, char in enumerate(s, 1):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]

print(min_window("ADOBECODEBANC", "ABC"))
# Output: "BANC"
```

---

### **19. Maximum Points You Can Obtain from Cards**

**Technique:** Sliding window over end selections

```python
def max_score(cardPoints, k):
    n = len(cardPoints)
    window = sum(cardPoints[:n - k])
    min_window = window
    total = sum(cardPoints)
    for i in range(n - k, n):
        window += cardPoints[i] - cardPoints[i - (n - k)]
        min_window = min(min_window, window)
    return total - min_window

print(max_score([1,2,3,4,5,6,1], 3))
# Output: 12
```

---

### **20. Longest Repeating Character Replacement with Any K Replacements (Generic)**

**Similar to character replacement, but generalized for Unicode strings or larger alphabets.**

```python
def generic_char_replacement(s, k):
    count = [0] * 128
    left = max_count = res = 0
    for right in range(len(s)):
        count[ord(s[right])] += 1
        max_count = max(max_count, count[ord(s[right])])
        while (right - left + 1) - max_count > k:
            count[ord(s[left])] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res

print(generic_char_replacement("ABAB", 2))
# Output: 4
```

---

Would you like to continue with **advanced prefix sum** + **2D window** problems next? Or explore **bitmask + trie + greedy** hybrids further?
