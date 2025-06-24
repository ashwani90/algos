Sure! Here are **10 beginner-level two pointers problems** with detailed solutions and explanations in Python:

---

### 1. **Two Sum II - Input Array Is Sorted**

**Problem:**
Given a sorted array, find two numbers that add up to a target.

**Explanation:**
Use two pointers, one at the start and one at the end. If sum is too small, move start pointer forward; if too large, move end pointer backward.

```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]  # 1-based indexing
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

# Example
print(twoSum([2,7,11,15], 9))  # Output: [1, 2]
```

---

### 2. **Remove Duplicates from Sorted Array**

**Problem:**
Remove duplicates in-place from a sorted array and return new length.

**Explanation:**
Use two pointers: one for iteration, one for position of unique elements.

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Example
nums = [1,1,2]
length = removeDuplicates(nums)
print(nums[:length])  # Output: [1, 2]
```

---

### 3. **Valid Palindrome**

**Problem:**
Check if a string is a palindrome considering only alphanumeric characters.

**Explanation:**
Use two pointers moving inward, skipping non-alphanumeric characters.

```python
def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# Example
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
```

---

### 4. **Merge Sorted Array**

**Problem:**
Merge two sorted arrays, with first having enough space at the end.

**Explanation:**
Start merging from the end using two pointers from the back.

```python
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Example
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1, 3, nums2, 3)
print(nums1)  # Output: [1,2,2,3,5,6]
```

---

### 5. **Reverse String**

**Problem:**
Reverse an array of characters in-place.

**Explanation:**
Use two pointers from both ends swapping characters.

```python
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Example
s = ["h","e","l","l","o"]
reverseString(s)
print(s)  # Output: ["o","l","l","e","h"]
```

---

### 6. **Remove Element**

**Problem:**
Remove all instances of a given value in-place and return the new length.

**Explanation:**
Use two pointers: one for iteration, one for placing valid elements.

```python
def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# Example
nums = [3,2,2,3]
length = removeElement(nums, 3)
print(nums[:length])  # Output: [2,2]
```

---

### 7. **Squares of a Sorted Array**

**Problem:**
Given a sorted array, return a new array of squares sorted.

**Explanation:**
Use two pointers from start and end, placing larger squares from the end.

```python
def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1
        pos -= 1
    return result

# Example
print(sortedSquares([-4,-1,0,3,10]))  # Output: [0,1,9,16,100]
```

---

### 8. **Two Sum - Less than Target**

**Problem:**
Count pairs whose sum is less than a target.

**Explanation:**
Use two pointers from start and end, count pairs when sum < target.

```python
def twoSumLessThanTarget(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0
    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1
    return count

# Example
print(twoSumLessThanTarget([3,1,2,4], 6))  # Output: 4
```

---

### 9. **Intersection of Two Arrays II**

**Problem:**
Return intersection of two arrays (including duplicates).

**Explanation:**
Sort both arrays, use two pointers to find common elements.

```python
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i = j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result

# Example
print(intersect([1,2,2,1], [2,2]))  # Output: [2,2]
```

---

### 10. **Longest Substring Without Repeating Characters**

**Problem:**
Find length of longest substring without repeating characters.

**Explanation:**
Use sliding window with two pointers and a hash map to track last occurrence.

```python
def lengthOfLongestSubstring(s):
    seen = {}
    left = max_len = 0
    for right, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1
        seen[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# Example
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
```

---

If you want, I can give you explanations for any specific problem or more problems!
