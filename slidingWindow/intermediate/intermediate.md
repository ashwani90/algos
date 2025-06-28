Here are **10 intermediate-level sliding window problems** with detailed **Python solutions** and **step-by-step explanations**. These will help you practice more sophisticated uses of the sliding window technique with hashmaps, condition tracking, and two-pointer optimizations.

---

### **1. Longest Substring with At Most K Distinct Characters**

**Problem:**
Given a string `s` and an integer `k`, return the length of the longest substring that contains at most `k` distinct characters.

**Solution:**

```python
def length_of_longest_substring_k_distinct(s, k):
    from collections import defaultdict
    left = 0
    max_len = 0
    char_count = defaultdict(int)

    for right in range(len(s)):
        char_count[s[right]] += 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(length_of_longest_substring_k_distinct("eceba", 2))  # Output: 3
```

**Explanation:**
Use a hashmap to track character frequencies, and shrink the window when distinct characters exceed `k`.

---

### **2. Fruits into Baskets**

**Problem:**
You are given an array where each element is a type of fruit. Pick at most two types of fruits such that the subarray is longest.

**Solution:**

```python
def total_fruit(fruits):
    from collections import defaultdict
    left = 0
    max_len = 0
    count = defaultdict(int)

    for right in range(len(fruits)):
        count[fruits[right]] += 1
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(total_fruit([1,2,1,2,3]))  # Output: 4
```

**Explanation:**
Same as previous, but with max 2 types allowed.

---

### **3. Longest Repeating Character Replacement**

**Problem:**
Find the length of the longest substring where you can replace at most `k` characters to make all characters the same.

**Solution:**

```python
def character_replacement(s, k):
    from collections import defaultdict
    left = 0
    max_len = 0
    count = defaultdict(int)
    max_count = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])
        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(character_replacement("ABAB", 2))  # Output: 4
```

**Explanation:**
The trick is to track the max frequency char and adjust the window when replacement count exceeds `k`.

---

### **4. Count Occurrences of Anagrams**

**Problem:**
Count how many times an anagram of `p` appears in string `s`.

**Solution:**

```python
from collections import Counter

def count_anagrams(s, p):
    p_count = Counter(p)
    s_count = Counter()
    res = 0
    k = len(p)

    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= k:
            s_count[s[i - k]] -= 1
            if s_count[s[i - k]] == 0:
                del s_count[s[i - k]]
        if s_count == p_count:
            res += 1
    return res

print(count_anagrams("cbaebabacd", "abc"))  # Output: 2
```

**Explanation:**
Use counters to check matching frequency in sliding windows.

---

### **5. Maximum Points You Can Obtain from Cards**

**Problem:**
Pick `k` cards from the front or end of the array to maximize the total points.

**Solution:**

```python
def max_score(cardPoints, k):
    total = sum(cardPoints[:k])
    max_score = total
    for i in range(1, k + 1):
        total += cardPoints[-i] - cardPoints[k - i]
        max_score = max(max_score, total)
    return max_score

print(max_score([1,2,3,4,5,6,1], 3))  # Output: 12
```

**Explanation:**
Pick from front and remove from start while adding from end.

---

### **6. Longest Subarray with Sum at Most K (Positive Integers)**

**Problem:**
Find longest subarray with sum ≤ `k`.

**Solution:**

```python
def longest_subarray_sum_k(arr, k):
    left = 0
    total = 0
    max_len = 0
    for right in range(len(arr)):
        total += arr[right]
        while total > k:
            total -= arr[left]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(longest_subarray_sum_k([1, 2, 3, 4, 5], 9))  # Output: 3 ([2,3,4])
```

**Explanation:**
Shrink from left until sum becomes ≤ `k`.

---

### **7. Maximum Number of Consecutive 1's with One Flip**

**Problem:**
Given a binary array, return max consecutive 1’s if you can flip at most one 0.

**Solution:**

```python
def max_consecutive_ones(nums):
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(max_consecutive_ones([1,0,1,1,0]))  # Output: 4
```

**Explanation:**
Allow one zero in the window; shrink if more.

---

### **8. Binary Subarrays With Sum**

**Problem:**
Return number of subarrays with sum equal to `goal`.

**Solution:**

```python
from collections import defaultdict

def num_subarrays_with_sum(nums, goal):
    prefix = defaultdict(int)
    prefix[0] = 1
    total = 0
    count = 0
    for num in nums:
        total += num
        count += prefix[total - goal]
        prefix[total] += 1
    return count

print(num_subarrays_with_sum([1,0,1,0,1], 2))  # Output: 4
```

**Explanation:**
Prefix sum + hashmap to count previous prefix sums.

---

### **9. Longest Subarray with At Most K 0s (Flip Zeroes)**

**Problem:**
Find the longest subarray where you can flip at most `k` 0s to 1.

**Solution:**

```python
def longest_ones(nums, k):
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2))  # Output: 6
```

**Explanation:**
Sliding window with a limit on number of 0s.

---

### **10. Max Consecutive Ones III (Flipping at Most K Zeros)**

**Problem:**
Variation where you flip `k` 0s to 1s to get the longest 1s subarray.

**Solution:**

```python
def longest_ones(nums, k):
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

print(longest_ones([0,0,1,1,1,0,0], 0))  # Output: 3
```

**Explanation:**
Use a two-pointer sliding window, shrinking when flips exceed `k`.

---

Would you like to proceed to **advanced sliding window problems** next?
