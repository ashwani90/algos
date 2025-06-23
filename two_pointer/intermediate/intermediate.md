Sure! Here are **10 intermediate-level two pointers problems** with detailed solutions and explanations in Python:

---

### 1. **3Sum**

**Problem:**
Find all unique triplets in an array which sum to zero.

**Explanation:**
Sort the array. Fix one element, then use two pointers to find pairs that sum to the negative of the fixed element.

```python
def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res

# Example
print(threeSum([-1,0,1,2,-1,-4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]
```

---

### 2. **Container With Most Water**

**Problem:**
Given n non-negative integers representing heights, find two lines that together with x-axis forms a container with the most water.

**Explanation:**
Use two pointers at both ends. Move the pointer with smaller height inward.

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        max_area = max(max_area, min(height[left], height[right]) * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Example
print(maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
```

---

### 3. **Trapping Rain Water**

**Problem:**
Given an elevation map, compute how much water it can trap after raining.

**Explanation:**
Use two pointers, track max left and max right heights, and accumulate trapped water accordingly.

```python
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

# Example
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
```

---

### 4. **Minimum Size Subarray Sum**

**Problem:**
Find the minimal length of a contiguous subarray of which the sum ≥ target.

**Explanation:**
Use sliding window expanding and contracting pointers.

```python
def minSubArrayLen(target, nums):
    left = total = 0
    min_len = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len

# Example
print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
```

---

### 5. **Longest Substring with At Most K Distinct Characters**

**Problem:**
Find length of longest substring containing at most K distinct characters.

**Explanation:**
Use sliding window with a hashmap tracking counts.

```python
def lengthOfLongestSubstringKDistinct(s, k):
    from collections import defaultdict
    count = defaultdict(int)
    left = max_len = 0
    for right in range(len(s)):
        count[s[right]] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# Example
print(lengthOfLongestSubstringKDistinct("eceba", 2))  # Output: 3
```

---

### 6. **Sort Colors (Dutch National Flag Problem)**

**Problem:**
Sort array of 0s, 1s, and 2s in-place.

**Explanation:**
Use three pointers: low, mid, high. Swap accordingly.

```python
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example
nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)  # Output: [0,0,1,1,2,2]
```

---

### 7. **Find All Anagrams in a String**

**Problem:**
Find all start indices of p's anagrams in s.

**Explanation:**
Use sliding window with count of characters.

```python
def findAnagrams(s, p):
    from collections import Counter
    p_count = Counter(p)
    s_count = Counter()
    result = []
    left = 0
    for right in range(len(s)):
        s_count[s[right]] += 1
        if right - left + 1 > len(p):
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1
        if s_count == p_count:
            result.append(left)
    return result

# Example
print(findAnagrams("cbaebabacd", "abc"))  # Output: [0,6]
```

---

### 8. **Valid Palindrome II**

**Problem:**
Check if a string can be palindrome by removing at most one character.

**Explanation:**
Use two pointers, if mismatch occurs try skipping either left or right char and check palindrome.

```python
def validPalindrome(s):
    def is_palindrome_range(i, j):
        return all(s[k] == s[j-k+i] for k in range(i, j))
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left+1, right) or is_palindrome_range(left, right-1)
        left += 1
        right -= 1
    return True

# Example
print(validPalindrome("abca"))  # Output: True
```

---

### 9. **Maximum Number of K-Sum Pairs**

**Problem:**
Find max number of pairs in array whose sum equals k.

**Explanation:**
Sort array, use two pointers to find pairs.

```python
def maxOperations(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0
    while left < right:
        s = nums[left] + nums[right]
        if s == k:
            count += 1
            left += 1
            right -= 1
        elif s < k:
            left += 1
        else:
            right -= 1
    return count

# Example
print(maxOperations([1,2,3,4], 5))  # Output: 2
```

---

### 10. **Longest Continuous Increasing Subsequence**

**Problem:**
Find length of longest continuous strictly increasing subsequence.

**Explanation:**
Use two pointers or iterate with count reset when sequence breaks.

```python
def findLengthOfLCIS(nums):
    if not nums:
        return 0
    max_len = 1
    current_len = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
    return max(max_len, current_len)

# Example
print(findLengthOfLCIS([1,3,5,4,7]))  # Output: 3
```

---

If you want me to explain any particular problem more or want more problems, just ask!
