Certainly! Here are **10 beginner-level hashmap problems** with detailed solutions and explanations.

---

## 1. Two Sum

**Problem:**
Given an array `nums` and a target value `target`, find indices of two numbers such that they add up to target.

**Solution:**

```python
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

# Example
print(twoSum([2,7,11,15], 9))  # Output: [0,1]
```

**Explanation:**
Store each number's index in hashmap. For each number, check if complement exists. This gives O(n) time complexity.

---

## 2. Contains Duplicate

**Problem:**
Check if any value appears at least twice in the array.

**Solution:**

```python
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example
print(containsDuplicate([1,2,3,1]))  # Output: True
```

**Explanation:**
Use a set to track seen numbers. If a number repeats, return True.

---

## 3. Intersection of Two Arrays II

**Problem:**
Given two arrays, return their intersection including duplicates.

**Solution:**

```python
def intersect(nums1, nums2):
    hashmap = {}
    res = []
    for num in nums1:
        hashmap[num] = hashmap.get(num, 0) + 1
    for num in nums2:
        if hashmap.get(num, 0) > 0:
            res.append(num)
            hashmap[num] -= 1
    return res

# Example
print(intersect([1,2,2,1], [2,2]))  # Output: [2,2]
```

**Explanation:**
Count elements in first array with hashmap, then check second array to find common elements.

---

## 4. Happy Number

**Problem:**
Write an algorithm to determine if a number is a "happy number". A number is happy if repeatedly replacing it by the sum of the squares of its digits eventually leads to 1.

**Solution:**

```python
def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

# Example
print(isHappy(19))  # Output: True
```

**Explanation:**
Use a set to detect loops. If loop detected before reaching 1, return False.

---

## 5. First Unique Character in a String

**Problem:**
Find the first non-repeating character in a string and return its index.

**Solution:**

```python
def firstUniqChar(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

# Example
print(firstUniqChar("leetcode"))  # Output: 0
```

**Explanation:**
Count occurrences using hashmap, then find the first character with count 1.

---

## 6. Valid Anagram

**Problem:**
Check if two strings are anagrams of each other.

**Solution:**

```python
def isAnagram(s, t):
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

# Example
print(isAnagram("anagram", "nagaram"))  # Output: True
```

**Explanation:**
Count characters of `s`, decrease for `t`, ensure no mismatches.

---

## 7. Ransom Note

**Problem:**
Given two strings `ransomNote` and `magazine`, check if ransomNote can be constructed from magazine.

**Solution:**

```python
def canConstruct(ransomNote, magazine):
    count = {}
    for c in magazine:
        count[c] = count.get(c, 0) + 1
    for c in ransomNote:
        if count.get(c, 0) == 0:
            return False
        count[c] -= 1
    return True

# Example
print(canConstruct("aa", "aab"))  # Output: True
```

**Explanation:**
Check character availability using hashmap.

---

## 8. Group Anagrams

**Problem:**
Group an array of strings into anagrams.

**Solution:**

```python
from collections import defaultdict

def groupAnagrams(strs):
    hashmap = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        hashmap[key].append(s)
    return list(hashmap.values())

# Example
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

**Explanation:**
Sort each string as key; group strings with same key.

---

## 9. Two Sum II - Input array is sorted

**Problem:**
Find two numbers that add to target in sorted array and return their indices (1-indexed).

**Solution:**

```python
def twoSumSorted(numbers, target):
    hashmap = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement] + 1, i + 1]
        hashmap[num] = i
    return []

# Example
print(twoSumSorted([2,7,11,15], 9))  # Output: [1,2]
```

**Explanation:**
Same as Two Sum but applied on sorted array.

---

## 10. Majority Element

**Problem:**
Find the element that appears more than n/2 times in the array.

**Solution:**

```python
def majorityElement(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums) // 2:
            return num

# Example
print(majorityElement([3,2,3]))  # Output: 3
```

**Explanation:**
Count elements until one surpasses half the array size.

---

If you'd like me to provide intermediate or advanced hashmap problems or more detail on any of these, just ask!
