Sure! Here are **10 beginner-level prefix sum problems** with detailed explanations and Python solutions:

---

### 1. **Running Sum of 1D Array**

**Problem:**
Given an array `nums`, return the running sum where `runningSum[i]` = sum of `nums[0]` to `nums[i]`.

**Explanation:**
Prefix sum at index `i` is sum of all elements up to `i`.

```python
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

# Example
print(runningSum([1,2,3,4]))  # Output: [1,3,6,10]
```

---

### 2. **Find Pivot Index**

**Problem:**
Find the index where the sum of elements to the left equals the sum of elements to the right.

**Explanation:**
Calculate total sum. Iterate and keep track of prefix sum; check if `left_sum == total_sum - left_sum - nums[i]`.

```python
def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total - left_sum - num:
            return i
        left_sum += num
    return -1

# Example
print(pivotIndex([1,7,3,6,5,6]))  # Output: 3
```

---

### 3. **Subarray Sum Equals K**

**Problem:**
Find the number of continuous subarrays whose sum equals k.

**Explanation:**
Use prefix sums and a hashmap to count how many prefix sums satisfy sum\[j] - sum\[i] = k.

```python
def subarraySum(nums, k):
    count = 0
    curr_sum = 0
    prefix_sums = {0:1}
    for num in nums:
        curr_sum += num
        count += prefix_sums.get(curr_sum - k, 0)
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
    return count

# Example
print(subarraySum([1,1,1], 2))  # Output: 2
```

---

### 4. **Range Sum Query - Immutable**

**Problem:**
Given an array `nums`, create a function to return sum of elements between indices `i` and `j`.

**Explanation:**
Precompute prefix sums for O(1) query.

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, i, j):
        return self.prefix[j+1] - self.prefix[i]

# Example
obj = NumArray([1,2,3,4])
print(obj.sumRange(1,3))  # Output: 9 (2+3+4)
```

---

### 5. **Max Consecutive Ones**

**Problem:**
Find the maximum number of consecutive 1s in a binary array.

**Explanation:**
Use prefix sums to store counts of consecutive ones or simply iterate and reset count on zero.

```python
def findMaxConsecutiveOnes(nums):
    max_count = count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

# Example
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3
```

---

### 6. **Count Nice Pairs in Array**

**Problem:**
Count pairs `(i, j)` where `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`.

**Explanation:**
Use prefix sum logic with a hashmap keyed by difference.

```python
def rev(x):
    return int(str(x)[::-1])

def countNicePairs(nums):
    count_map = {}
    count = 0
    mod = 10**9 + 7
    for num in nums:
        key = num - rev(num)
        count += count_map.get(key, 0)
        count_map[key] = count_map.get(key, 0) + 1
    return count % mod

# Example
print(countNicePairs([42,11,1,97]))  # Output: 2
```

---

### 7. **Number of Subarrays with Bounded Maximum**

**Problem:**
Count number of subarrays where max element is between left and right.

**Explanation:**
Use prefix sums to count total subarrays and subtract those out of bounds.

```python
def numSubarrayBoundedMax(nums, left, right):
    def count(bound):
        res = cur = 0
        for num in nums:
            cur = cur + 1 if num <= bound else 0
            res += cur
        return res
    return count(right) - count(left - 1)

# Example
print(numSubarrayBoundedMax([2,1,4,3], 2, 3))  # Output: 3
```

---

### 8. **Find the Missing Number**

**Problem:**
Find the missing number in a list from 0 to n.

**Explanation:**
Use prefix sums: total sum - actual sum.

```python
def missingNumber(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)

# Example
print(missingNumber([3,0,1]))  # Output: 2
```

---

### 9. **Binary Subarrays With Sum**

**Problem:**
Count the number of subarrays with sum equal to `goal` in a binary array.

**Explanation:**
Use prefix sums and a hashmap to count subarrays with desired sums.

```python
def numSubarraysWithSum(nums, goal):
    count_map = {0:1}
    curr_sum = 0
    count = 0
    for num in nums:
        curr_sum += num
        count += count_map.get(curr_sum - goal, 0)
        count_map[curr_sum] = count_map.get(curr_sum, 0) + 1
    return count

# Example
print(numSubarraysWithSum([1,0,1,0,1], 2))  # Output: 4
```

---

### 10. **How Many Numbers Are Smaller Than the Current Number**

**Problem:**
For each number in nums, count how many numbers are smaller than it.

**Explanation:**
Use prefix sums to store frequencies and cumulative counts.

```python
def smallerNumbersThanCurrent(nums):
    count = [0]*101
    for num in nums:
        count[num] += 1
    for i in range(1, 101):
        count[i] += count[i-1]
    return [count[num-1] if num > 0 else 0 for num in nums]

# Example
print(smallerNumbersThanCurrent([8,1,2,2,3]))  # Output: [4,0,1,1,3]
```

---

If you want me to explain any specific problem in more detail or provide more examples, feel free to ask!
