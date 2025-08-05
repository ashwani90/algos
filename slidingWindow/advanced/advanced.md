### **2. Minimum Window Substring**

**Problem:**
Find the smallest substring of `s` that contains all characters of `t`.

**Solution:**

```python
from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)
    required = len(t_count)
    formed = 0
    l, r = 0, 0
    window_counts = {}
    ans = float("inf"), None, None

    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        while l <= r and formed == required:
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[s[l]] -= 1
            if s[l] in t_count and window_counts[s[l]] < t_count[s[l]]:
                formed -= 1
            l += 1

        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

print(min_window("ADOBECODEBANC", "ABC"))
# Output: "BANC"
```

**Explanation:**
Expand and shrink the window while maintaining character counts.

---

### **3. Count Number of Nice Subarrays**

**Problem:**
Find number of subarrays with exactly `k` odd numbers.

**Solution:**

```python
from collections import defaultdict

def number_of_subarrays(nums, k):
    count = defaultdict(int)
    count[0] = 1
    odd = 0
    result = 0

    for num in nums:
        odd += num % 2
        result += count[odd - k]
        count[odd] += 1
    return result

print(number_of_subarrays([1,1,2,1,1], 3))
# Output: 2
```

**Explanation:**
Convert the problem into prefix sum with count of odd numbers.

---

### **4. Longest Substring with At Most K Unique Characters**

**Problem:**
Find the longest substring with at most `k` unique characters.

**Solution:**

```python
from collections import defaultdict

def longest_k_substring(s, k):
    left = 0
    char_map = defaultdict(int)
    max_len = 0

    for right in range(len(s)):
        char_map[s[right]] += 1
        while len(char_map) > k:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(longest_k_substring("aaabbcc", 2))
# Output: 5
```

---

### **5. Subarrays with K Different Integers**

**Problem:**
Return the number of subarrays with exactly `k` different integers.

**Solution:**

```python
from collections import defaultdict

def at_most_k(nums, k):
    count = defaultdict(int)
    res = left = 0
    for right in range(len(nums)):
        if count[nums[right]] == 0:
            k -= 1
        count[nums[right]] += 1
        while k < 0:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                k += 1
            left += 1
        res += right - left + 1
    return res

def subarrays_with_k_distinct(nums, k):
    return at_most_k(nums, k) - at_most_k(nums, k - 1)

print(subarrays_with_k_distinct([1,2,1,2,3], 2))
# Output: 7
```

**Explanation:**
Use inclusion-exclusion with at most `k` and `k - 1`.

---

### **6. Longest Repeating Character Replacement (Advanced Variant)**

**Problem:**
Allow up to `k` character changes to maximize substring with same characters.

**Solution:**
Already solved in intermediate-level list.

---

### **7. Maximum Average Subarray of Size K**

**Problem:**
Find the contiguous subarray of size `k` with the maximum average.

**Solution:**

```python
def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    max_avg = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_avg = max(max_avg, window_sum)
    return max_avg / k

print(find_max_average([1,12,-5,-6,50,3], 4))
# Output: 12.75
```

---

### **8. Shortest Subarray with Sum at Least K (Mixed Prefix + Deque)**

**Problem:**
Find shortest subarray with sum ≥ `k`.

**Solution:**

```python
from collections import deque

def shortest_subarray(nums, k):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    dq = deque()
    res = float('inf')
    for i in range(len(prefix)):
        while dq and prefix[i] - prefix[dq[0]] >= k:
            res = min(res, i - dq.popleft())
        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()
        dq.append(i)
    return res if res != float('inf') else -1

print(shortest_subarray([2,-1,2], 3))
# Output: 3
```

---

### **9. Max Consecutive Ones III**

**Problem:**
Flip at most `k` zeros to get longest 1’s subarray.

**Solution:**
Already solved in intermediate-level list.

---

### **10. Maximum Sum of Distinct Subarray with Length K**

**Problem:**
Find max sum of subarray of size `k` with all distinct elements.

**Solution:**

```python
def maximum_subarray_sum(nums, k):
    seen = set()
    left = 0
    curr_sum = 0
    max_sum = 0

    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
        seen.add(nums[right])
        curr_sum += nums[right]
        if right - left + 1 == k:
            max_sum = max(max_sum, curr_sum)
            seen.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
    return max_sum

print(maximum_subarray_sum([1,2,1,3,4], 3))
# Output: 8
```

---

Would you like 10 more expert-level variations or contests combining sliding window with DP or bitmasking?
