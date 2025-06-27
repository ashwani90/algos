Got it! Here are **10 intermediate-level bitmask problems** with detailed solutions and explanations in Python:

---

### 1. **Find All Subsets of a Set**

**Problem:**
Given a set of distinct integers, print all possible subsets.

**Solution:**

```python
def subsets(nums):
    n = len(nums)
    all_subsets = []
    for mask in range(1 << n):  # 2^n masks
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        all_subsets.append(subset)
    return all_subsets

print(subsets([1, 2, 3]))
```

**Explanation:**
Each subset corresponds to a bitmask where bit `i` is set if `nums[i]` is in the subset. Loop over all masks from `0` to `2^n - 1` to generate subsets.

---

### 2. **Count Subsets with Given Sum**

**Problem:**
Given an array and sum `S`, count subsets that sum to `S`.

**Solution:**

```python
def count_subsets_with_sum(nums, S):
    count = 0
    n = len(nums)
    for mask in range(1 << n):
        subset_sum = 0
        for i in range(n):
            if mask & (1 << i):
                subset_sum += nums[i]
        if subset_sum == S:
            count += 1
    return count

print(count_subsets_with_sum([1, 2, 3], 3))  # 2 ([1,2] and [3])
```

**Explanation:**
Generate all subsets with bitmask, calculate sum for each, and count those equal to `S`.

---

### 3. **Find the Missing Number Using Bitmask**

**Problem:**
Given an array containing numbers from 0 to n with one number missing, find the missing number.

**Solution:**

```python
def missing_number(nums):
    n = len(nums)
    xor_all = 0
    xor_arr = 0
    for i in range(n + 1):
        xor_all ^= i
    for num in nums:
        xor_arr ^= num
    return xor_all ^ xor_arr

print(missing_number([0, 1, 3]))  # 2
```

**Explanation:**
XOR of all numbers from 0 to n and XOR of array elements; missing number is XOR of these two results.

---

### 4. **Check if a Subset Sum Exists (Using Bitmask DP)**

**Problem:**
Given array `nums` and sum `S`, check if any subset sums to `S` using bitmask DP.

**Solution:**

```python
def subset_sum(nums, S):
    n = len(nums)
    possible = [False] * (S + 1)
    possible[0] = True
    for num in nums:
        for s in range(S, num - 1, -1):
            if possible[s - num]:
                possible[s] = True
    return possible[S]

print(subset_sum([3, 34, 4, 12, 5, 2], 9))  # True
```

**Explanation:**
Classic subset sum solved using DP; bitmask representation is implicit in state tracking which sums are possible.

---

### 5. **Count Set Bits in All Numbers from 0 to N**

**Problem:**
Return an array where each element is the count of set bits in numbers from 0 to N.

**Solution:**

```python
def count_bits(n):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    return result

print(count_bits(5))  # [0,1,1,2,1,2]
```

**Explanation:**
Use the relation `bits(i) = bits(i//2) + i%2`. Right shift halves the number; add last bit.

---

### 6. **Find Two Numbers with Odd Occurrences**

**Problem:**
Given an array where all numbers occur even times except two numbers, find those two numbers.

**Solution:**

```python
def find_two_odd_occurrences(arr):
    xor_all = 0
    for num in arr:
        xor_all ^= num
    # Find rightmost set bit
    set_bit = xor_all & -xor_all
    x = 0
    y = 0
    for num in arr:
        if num & set_bit:
            x ^= num
        else:
            y ^= num
    return x, y

print(find_two_odd_occurrences([2, 3, 7, 9, 2, 3, 7, 11]))  # (9, 11)
```

**Explanation:**
XOR all numbers gives XOR of two odd occurring numbers. Use set bit to divide into two groups and XOR separately.

---

### 7. **Subset XOR Queries**

**Problem:**
Given array and queries, for each query find XOR of all elements in the subset specified by bitmask.

**Solution:**

```python
def subset_xor(nums, queries):
    results = []
    for mask in queries:
        xor_sum = 0
        for i in range(len(nums)):
            if mask & (1 << i):
                xor_sum ^= nums[i]
        results.append(xor_sum)
    return results

print(subset_xor([1,2,3], [0, 1, 5]))  # [0,1,2]
```

**Explanation:**
Use bitmask to select subset elements and XOR them.

---

### 8. **Count Numbers with Exactly k Set Bits up to N**

**Problem:**
Count how many numbers from 0 to N have exactly k set bits.

**Solution:**

```python
def count_k_set_bits(N, k):
    count = 0
    for i in range(N + 1):
        if bin(i).count('1') == k:
            count += 1
    return count

print(count_k_set_bits(10, 2))  # 5 (3,5,6,9,10)
```

**Explanation:**
Iterate all numbers and count bits, increment if bits == k.

---

### 9. **Find if a Number is a Sum of Two Powers of Two**

**Problem:**
Given `n`, check if it can be represented as the sum of two powers of two.

**Solution:**

```python
def sum_of_two_powers(n):
    for i in range(31):
        for j in range(i, 31):
            if (1 << i) + (1 << j) == n:
                return True
    return False

print(sum_of_two_powers(10))  # True (8 + 2)
print(sum_of_two_powers(7))   # False
```

**Explanation:**
Try all pairs of powers of two; if sum matches n, return True.

---

### 10. **Maximum AND of Any Two Numbers in an Array**

**Problem:**
Find the maximum AND value of any two numbers in the array.

**Solution:**

```python
def max_and_pair(nums):
    max_and = 0
    for bit in reversed(range(32)):
        temp = max_and | (1 << bit)
        count = 0
        for num in nums:
            if (num & temp) == temp:
                count += 1
        if count >= 2:
            max_and = temp
    return max_and

print(max_and_pair([4, 8, 12, 16]))  # 8
```

**Explanation:**
Try setting bits from highest to lowest; keep only bits that appear in at least two numbers.

---

If you'd like, I can continue with advanced bitmask problems or other topics!
