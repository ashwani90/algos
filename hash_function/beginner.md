Sure! Here are **10 hash function problems** with detailed solutions and explanations in Python. These problems focus on using hashing techniques such as hash maps (dictionaries), rolling hashes, and string hashing to solve common algorithmic tasks.

---

## 1. Two Sum

**Problem:**
Given an array `nums` and a target `target`, find indices of two numbers such that they add up to `target`.

**Solution:**

```python
def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []

print(two_sum([2,7,11,15], 9))  # Output: [0,1]
```

**Explanation:**
We use a hash map to store each number's index. For each number, check if its complement exists in the map, which gives O(n) time.

---

## 2. Check Anagrams

**Problem:**
Given two strings, determine if they are anagrams of each other.

**Solution:**

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count or count[c] == 0:
            return False
        count[c] -= 1
    return True

print(is_anagram("listen", "silent"))  # Output: True
```

**Explanation:**
Use a hash map to count characters in one string and then decrease counts for the other string, checking for mismatches.

---

## 3. Subarray Sum Equals K

**Problem:**
Given an integer array and integer `k`, find the total number of continuous subarrays whose sum equals to `k`.

**Solution:**

```python
def subarray_sum(nums, k):
    count = 0
    curr_sum = 0
    prefix_sums = {0:1}
    
    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix_sums:
            count += prefix_sums[curr_sum - k]
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
    return count

print(subarray_sum([1,1,1], 2))  # Output: 2
```

**Explanation:**
We keep track of prefix sums and their counts. If the difference `(curr_sum - k)` appeared before, it means a subarray sums to `k`.

---

## 4. Longest Consecutive Sequence

**Problem:**
Given an unsorted array, find the length of the longest consecutive elements sequence.

**Solution:**

```python
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:  # start of sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

print(longest_consecutive([100,4,200,1,3,2]))  # Output: 4
```

**Explanation:**
By storing elements in a hash set, we efficiently check the start of a consecutive sequence and count its length.

---

## 5. Group Anagrams

**Problem:**
Group an array of strings into anagrams.

**Solution:**

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

**Explanation:**
We use a sorted tuple of the string characters as the hash key to group anagrams efficiently.

---

## 6. Count Distinct Elements in Every Window of Size K

**Problem:**
Given an array and window size `k`, find the count of distinct elements in every window.

**Solution:**

```python
from collections import defaultdict

def count_distinct_in_windows(arr, k):
    count_map = defaultdict(int)
    result = []
    distinct_count = 0
    
    for i in range(len(arr)):
        if count_map[arr[i]] == 0:
            distinct_count += 1
        count_map[arr[i]] += 1
        
        if i >= k:
            count_map[arr[i-k]] -= 1
            if count_map[arr[i-k]] == 0:
                distinct_count -= 1
                
        if i >= k - 1:
            result.append(distinct_count)
    return result

print(count_distinct_in_windows([1,2,1,3,4,2,3], 4))  # Output: [3,4,4,3]
```

**Explanation:**
Maintain a sliding window with a frequency map; update distinct counts as elements enter/exit window.

---

## 7. Detect Cycle in a Directed Graph using Hashing (Visited Sets)

**Problem:**
Detect if a directed graph contains a cycle.

**Solution:**

```python
def detect_cycle(graph):
    visited = set()
    rec_stack = set()
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

graph = {1:[2], 2:[3], 3:[1]}
print(detect_cycle(graph))  # Output: True
```

**Explanation:**
Use hashing to track visited nodes and recursion stack to detect back edges indicating cycles.

---

## 8. Rolling Hash for String Pattern Matching (Rabin-Karp Algorithm)

**Problem:**
Find all occurrences of a pattern in a text string.

**Solution:**

```python
def rabin_karp(text, pattern):
    d = 256
    q = 101  # a prime number for modulus
    n, m = len(text), len(pattern)
    h = pow(d, m-1) % q
    p_hash = 0
    t_hash = 0
    result = []

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i+m] == pattern:
                result.append(i)
        if i < n - m:
            t_hash = (d*(t_hash - ord(text[i])*h) + ord(text[i+m])) % q
            if t_hash < 0:
                t_hash += q
    return result

print(rabin_karp("abracadabra", "abra"))  # Output: [0, 7]
```

**Explanation:**
Use polynomial rolling hash to compare substring hashes in O(1) time, drastically reducing time complexity.

---

## 9. Count Palindromic Substrings Using Hashing

**Problem:**
Count all palindromic substrings in a string.

**Solution (Outline):**
Precompute forward and backward prefix hashes with rolling hash. Check substring hashes to detect palindrome in O(1).

---

## 10. Longest Duplicate Substring Using Binary Search + Rolling Hash

**Problem:**
Find the longest substring that appears at least twice in the string.

**Solution (Outline):**
Use binary search on length and rolling hash to detect duplicates of a given length.

---

If you want me to provide full code and detailed step-by-step solutions for problems #9 and #10 or any other, just say!
