Here are **10 beginner-level sliding window problems** with detailed **explanations and Python solutions**. These problems help in understanding how to use the sliding window technique for arrays and strings efficiently.

---

### **1. Maximum Sum Subarray of Size K**

**Problem:**
Given an array of integers and a number `k`, find the maximum sum of any contiguous subarray of size `k`.

**Solution:**

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9
```

**Explanation:**
Start with the sum of the first `k` elements, then slide the window by removing the first element and adding the next one.

---

### **2. Minimum Size Subarray Sum**

**Problem:**
Given an array of positive integers and a number `s`, find the minimal length of a subarray for which the sum is at least `s`.

**Solution:**

```python
def min_subarray_len(s, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= s:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

print(min_subarray_len(7, [2,3,1,2,4,3]))  # Output: 2
```

**Explanation:**
Expand the right pointer and shrink the left pointer when the sum is enough.

---

### **3. Longest Substring Without Repeating Characters**

**Problem:**
Given a string, find the length of the longest substring without repeating characters.

**Solution:**

```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

print(length_of_longest_substring("abcabcbb"))  # Output: 3
```

**Explanation:**
Use a set to keep track of characters. Slide left when a duplicate is found.

---

### **4. Maximum Number of Vowels in a Substring of Given Length**

**Problem:**
Given a string and an integer `k`, return the maximum number of vowels in any substring of length `k`.

**Solution:**

```python
def max_vowels(s, k):
    vowels = set('aeiou')
    count = sum(1 for c in s[:k] if c in vowels)
    max_count = count

    for i in range(k, len(s)):
        if s[i - k] in vowels:
            count -= 1
        if s[i] in vowels:
            count += 1
        max_count = max(max_count, count)

    return max_count

print(max_vowels("abciiidef", 3))  # Output: 3
```

**Explanation:**
Use a fixed-size window and count vowels as you move forward.

---

### **5. Find All Anagrams in a String**

**Problem:**
Find all start indices of `p`'s anagrams in `s`.

**Solution:**

```python
from collections import Counter

def find_anagrams(s, p):
    res = []
    p_count = Counter(p)
    s_count = Counter()

    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= len(p):
            s_count[s[i - len(p)]] -= 1
            if s_count[s[i - len(p)]] == 0:
                del s_count[s[i - len(p)]]
        if s_count == p_count:
            res.append(i - len(p) + 1)
    return res

print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
```

**Explanation:**
Compare frequency maps using `Counter` in a sliding window of size `len(p)`.

---

### **6. Sliding Window Maximum (Naive Beginner Version)**

**Problem:**
Return the maximum for each window of size `k` in the array.

**Solution:**

```python
def max_sliding_window(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        res.append(max(nums[i:i+k]))
    return res

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
```

**Explanation:**
Naively compute the max of each window. More efficient solutions use deque.

---

### **7. Count Number of Nice Subarrays**

**Problem:**
Return the number of subarrays with exactly `k` odd numbers.

**Solution:**

```python
def number_of_subarrays(nums, k):
    from collections import defaultdict
    prefix = defaultdict(int)
    prefix[0] = 1
    odd_count = result = 0

    for num in nums:
        odd_count += num % 2
        result += prefix[odd_count - k]
        prefix[odd_count] += 1

    return result

print(number_of_subarrays([1,1,2,1,1], 3))  # Output: 2
```

**Explanation:**
Use prefix sum + hashmap for the count of subarrays with a given number of odd numbers.

---

### **8. Average of All Subarrays of Size K**

**Problem:**
Return an array with averages of all contiguous subarrays of size `k`.

**Solution:**

```python
def avg_subarrays_of_k(arr, k):
    res = []
    window_sum = sum(arr[:k])
    res.append(window_sum / k)

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        res.append(window_sum / k)

    return res

print(avg_subarrays_of_k([1,3,2,6,-1,4,1,8,2], 5))
# Output: [2.2, 3.6, 2.8, 4.0, 4.4]
```

**Explanation:**
Use a sliding sum and divide by `k` at each step.

---

### **9. Substrings of Size K with K Distinct Characters**

**Problem:**
Return the count of substrings of size `k` that have `k` distinct characters.

**Solution:**

```python
def count_good_substrings(s, k):
    count = 0
    for i in range(len(s) - k + 1):
        if len(set(s[i:i+k])) == k:
            count += 1
    return count

print(count_good_substrings("havefunonleetcode", 3))  # Output: 6
```

**Explanation:**
Check every substring of size `k` for distinct characters.

---

### **10. Maximum Sum of a Subarray of Size Less Than or Equal to K**

**Problem:**
Find the maximum sum of any contiguous subarray with size ≤ `k`.

**Solution:**

```python
def max_sum_subarray_k_or_less(nums, k):
    max_sum = float('-inf')
    for size in range(1, k + 1):
        window_sum = sum(nums[:size])
        max_sum = max(max_sum, window_sum)
        for i in range(size, len(nums)):
            window_sum += nums[i] - nums[i - size]
            max_sum = max(max_sum, window_sum)
    return max_sum

print(max_sum_subarray_k_or_less([2, 1, 5, 1, 3, 2], 3))  # Output: 9
```

**Explanation:**
Try all window sizes from 1 to `k`.

---

Let me know if you want to practice on **intermediate** or **advanced** sliding window problems next!
