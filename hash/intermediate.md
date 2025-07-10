Sure! Here are **10 intermediate-level hashmap problems** along with detailed solutions and explanations.

---

### 1. **Subarray Sum Equals K**

**Problem:**
Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

**Solution:**

```python
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    hashmap = {0: 1}  # prefix_sum: frequency

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum - k]
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count

# Example
print(subarraySum([1,1,1], 2))  # Output: 2
```

**Explanation:**
Use prefix sums and hashmap to store frequencies of prefix sums. If `prefix_sum - k` is in hashmap, it means a subarray sums to `k`.

---

### 2. **Longest Consecutive Sequence**

**Problem:**
Given an unsorted array, find the length of the longest consecutive elements sequence.

**Solution:**

```python
def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in num_set:  # start of sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest

# Example
print(longestConsecutive([100,4,200,1,3,2]))  # Output: 4
```

**Explanation:**
Store numbers in a set for O(1) lookups. For each number, only start counting sequence if it’s the start (no predecessor).

---

### 3. **Group Shifted Strings**

**Problem:**
Group strings that belong to the same shifting sequence.

**Solution:**

```python
from collections import defaultdict

def groupStrings(strings):
    hashmap = defaultdict(list)

    for s in strings:
        key = []
        for i in range(1, len(s)):
            circular_diff = (ord(s[i]) - ord(s[i-1])) % 26
            key.append(str(circular_diff))
        hashmap[tuple(key)].append(s)

    return list(hashmap.values())

# Example
print(groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
# Output: [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]
```

**Explanation:**
Represent each string by difference of adjacent characters modulo 26. Group strings by this key.

---

### 4. **Find All Anagrams in a String**

**Problem:**
Find all start indices of p's anagrams in s.

**Solution:**

```python
from collections import Counter

def findAnagrams(s, p):
    res = []
    p_count = Counter(p)
    s_count = Counter()

    left = 0
    for right in range(len(s)):
        s_count[s[right]] += 1
        if right - left + 1 > len(p):
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1
        if s_count == p_count:
            res.append(left)

    return res

# Example
print(findAnagrams("cbaebabacd", "abc"))  # Output: [0,6]
```

**Explanation:**
Use sliding window + hashmap (Counter) to track character frequencies and find matching windows.

---

### 5. **Top K Frequent Elements**

**Problem:**
Return the k most frequent elements in the array.

**Solution:**

```python
from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Example
print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1,2]
```

**Explanation:**
Count frequency and use heapq.nlargest to get top k frequent keys efficiently.

---

### 6. **Longest Substring Without Repeating Characters**

**Problem:**
Find the length of the longest substring without repeating characters.

**Solution:**

```python
def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len

# Example
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
```

**Explanation:**
Use hashmap to store last seen index. Move left pointer to avoid duplicates and track max length.

---

### 7. **Minimum Window Substring**

**Problem:**
Given strings s and t, find the minimum window substring of s that contains all characters of t.

**Solution:**

```python
from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)
    formed = 0
    window_counts = {}
    left, right = 0, 0
    min_len = float('inf')
    ans = (None, None)

    while right < len(s):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1

        if c in dict_t and window_counts[c] == dict_t[c]:
            formed += 1

        while left <= right and formed == required:
            c = s[left]
            if right - left + 1 < min_len:
                min_len = right - left + 1
                ans = (left, right)

            window_counts[c] -= 1
            if c in dict_t and window_counts[c] < dict_t[c]:
                formed -= 1
            left += 1

        right += 1

    return "" if ans[0] is None else s[ans[0]:ans[1]+1]

# Example
print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
```

**Explanation:**
Use sliding window + hashmap to keep track of character counts and shrink window when all required chars are included.

---

### 8. **Find Duplicate Subtrees**

**Problem:**
Given a binary tree, return all duplicate subtrees (same structure and node values).

**Solution:**

```python
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDuplicateSubtrees(root):
    res = []
    count = defaultdict(int)

    def serialize(node):
        if not node:
            return '#'
        serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
        count[serial] += 1
        if count[serial] == 2:
            res.append(node)
        return serial

    serialize(root)
    return res
```

**Explanation:**
Serialize subtrees and track frequencies. If a serialization appears twice, subtree is duplicate.

---

### 9. **Subdomain Visit Count**

**Problem:**
Given counts of visits to domains, return counts for each subdomain.

**Solution:**

```python
from collections import defaultdict

def subdomainVisits(cpdomains):
    count = defaultdict(int)

    for domain in cpdomains:
        c, d = domain.split()
        c = int(c)
        fragments = d.split('.')
        for i in range(len(fragments)):
            subdomain = '.'.join(fragments[i:])
            count[subdomain] += c

    return [f"{v} {k}" for k, v in count.items()]

# Example
print(subdomainVisits(["9001 discuss.leetcode.com"]))
# Output: ["9001 discuss.leetcode.com","9001 leetcode.com","9001 com"]
```

**Explanation:**
Split domain into subdomains and accumulate counts for each.

---

### 10. **Longest Arithmetic Subsequence**

**Problem:**
Given an integer array, find the length of the longest arithmetic subsequence.

**Solution:**

```python
def longestArithSeqLength(nums):
    dp = [{} for _ in range(len(nums))]
    max_len = 0

    for i in range(len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            max_len = max(max_len, dp[i][diff])

    return max_len

# Example
print(longestArithSeqLength([3,6,9,12]))  # Output: 4
```

**Explanation:**
Use hashmap dp where dp\[i]\[diff] = length of arithmetic subsequence ending at i with difference diff.

---

If you'd like me to give more problems or focus on any specific topic, just let me know!
