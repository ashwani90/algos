Absolutely! Here are **10 advanced-level two pointers problems** with detailed solutions and explanations in Python:

---

### 1. **Longest Substring Without Repeating Characters**

**Problem:**
Find the length of the longest substring without repeating characters.

**Explanation:**
Use two pointers to create a sliding window and a hash map/set to track characters inside the window. Move right pointer expanding the window; when duplicate found, move left pointer until the duplicate is removed.

```python
def lengthOfLongestSubstring(s):
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

# Example
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
```

---

### 2. **Substring with Concatenation of All Words**

**Problem:**
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once without any intervening characters.

**Explanation:**
Use multiple sliding windows with two pointers plus a hashmap to count word frequencies. Slide through s with window size = total length of all words.

```python
def findSubstring(s, words):
    if not s or not words:
        return []
    word_len = len(words[0])
    word_count = len(words)
    substring_len = word_len * word_count
    word_freq = {}
    for w in words:
        word_freq[w] = word_freq.get(w, 0) + 1

    results = []

    for i in range(word_len):
        left = i
        right = i
        curr_count = {}
        count = 0
        while right + word_len <= len(s):
            word = s[right:right+word_len]
            right += word_len
            if word in word_freq:
                curr_count[word] = curr_count.get(word, 0) + 1
                count += 1
                while curr_count[word] > word_freq[word]:
                    left_word = s[left:left+word_len]
                    curr_count[left_word] -= 1
                    count -= 1
                    left += word_len
                if count == word_count:
                    results.append(left)
            else:
                curr_count.clear()
                count = 0
                left = right
    return results

# Example
print(findSubstring("barfoothefoobarman", ["foo","bar"]))  # Output: [0,9]
```

---

### 3. **Minimum Window Substring**

**Problem:**
Find the minimum window in s which contains all characters of t.

**Explanation:**
Use two pointers and a hashmap to track required chars, expand right pointer to include chars and contract left pointer to find minimum window.

```python
def minWindow(s, t):
    from collections import Counter
    if not s or not t:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t)

    left, right = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]

            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            left += 1
        right += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

# Example
print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
```

---

### 4. **Find K Pairs with Smallest Sums**

**Problem:**
You are given two sorted arrays nums1 and nums2. Find the k pairs (u,v) with the smallest sums.

**Explanation:**
Use two pointers and a min heap to efficiently get next smallest pairs.

```python
import heapq

def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []
    min_heap = []
    result = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
    while k > 0 and min_heap:
        total, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
        k -= 1
    return result

# Example
print(kSmallestPairs([1,7,11], [2,4,6], 3))  # Output: [[1,2],[1,4],[1,6]]
```

---

### 5. **Longest Repeating Character Replacement**

**Problem:**
Given a string s and integer k, find the length of the longest substring containing the same letter you can get after performing at most k replacements.

**Explanation:**
Use sliding window and keep track of max frequency char in the window to decide when to shrink window.

```python
def characterReplacement(s, k):
    count = {}
    max_count = max_len = left = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# Example
print(characterReplacement("AABABBA", 1))  # Output: 4
```

---

### 6. **Palindrome Pairs**

**Problem:**
Given a list of unique words, find all pairs of indices (i, j) such that words\[i] + words\[j] is a palindrome.

**Explanation:**
Use a hashmap to store words and check prefixes/suffixes for palindrome matches.

```python
def palindromePairs(words):
    def is_palindrome(check):
        return check == check[::-1]

    word_dict = {word: i for i, word in enumerate(words)}
    result = []

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]
            if is_palindrome(prefix):
                back = suffix[::-1]
                if back != word and back in word_dict:
                    result.append([word_dict[back], i])
            if j != len(word) and is_palindrome(suffix):
                back = prefix[::-1]
                if back != word and back in word_dict:
                    result.append([i, word_dict[back]])
    return result

# Example
print(palindromePairs(["abcd","dcba","lls","s","sssll"]))  
# Output: [[1,0],[0,1],[3,2],[2,4]]
```

---

### 7. **Split Array into Fibonacci Sequence**

**Problem:**
Given a string, split it into a Fibonacci-like sequence if possible.

**Explanation:**
Use backtracking with two pointers and integer overflow checks.

```python
def splitIntoFibonacci(S):
    def backtrack(index, seq):
        if index == len(S) and len(seq) >= 3:
            return seq
        num = 0
        for i in range(index, len(S)):
            if i > index and S[index] == '0':
                break
            num = num * 10 + int(S[i])
            if num > 2**31 - 1:
                break
            if len(seq) < 2 or num == seq[-1] + seq[-2]:
                res = backtrack(i + 1, seq + [num])
                if res:
                    return res
        return None
    return backtrack(0, []) or []

# Example
print(splitIntoFibonacci("11235813"))  # Output: [1,1,2,3,5,8,13]
```

---

### 8. **Minimum Number of Refueling Stops**

**Problem:**
Find minimum refueling stops to reach target distance given stations with fuel amounts.

**Explanation:**
Use two pointers and a max heap to greedily pick the largest fuel available before running out.

```python
import heapq

def minRefuelStops(target, startFuel, stations):
    heap = []
    stations.append((target, 0))
    fuel = startFuel
    prev = 0
    stops = 0

    for location, capacity in stations:
        fuel -= location - prev
        while fuel < 0 and heap:
            fuel += -heapq.heappop(heap)
            stops += 1
        if fuel < 0:
            return -1
        heapq.heappush(heap, -capacity)
        prev = location
    return stops

# Example
print(minRefuelStops(100, 10, [(10,60),(20,30),(30,30),(60,40)]))  # Output: 2
```

---

### 9. **Longest Duplicate Substring**

**Problem:**
Find the longest substring that appears at least twice.

**Explanation:**
Use binary search on substring length + rolling hash + two pointers to check duplicates efficiently.

```python
def longestDupSubstring(S):
    def check(L, a, modulus, n, nums):
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus
        seen = {h}
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

    n = len(S)
    nums = [ord(c) - ord('a') for c in S]
    a = 26
    modulus = 2**24
    left, right = 1, n
    start = -1
    while left <= right:
        L = left + (right - left) // 2
        idx = check(L, a, modulus, n, nums)
        if idx != -1:
            left = L + 1
            start = idx
        else:
            right = L - 1
    return S[start:start + left - 1] if start != -1 else ""

# Example
print(longestDupSubstring("banana"))  # Output: "ana"
```

---

### 10. **Sliding Window Maximum**

**Problem:**
Find maximum value in each sliding window of size k.

**Explanation:**
Use deque to maintain indices of useful elements in the current window.

```python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    result = []
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

# Example
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
```

---

If you want me to provide more problems, explanations, or help on a particular one, just let me know!
