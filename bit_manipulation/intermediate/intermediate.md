Here are **10 intermediate-level Bit Manipulation problems** with Python solutions and clear explanations. These go beyond basic checks and use bits to solve moderately complex problems efficiently.

---

### **1. Find Two Non-Repeating Elements in an Array**

**Problem**: Every element appears twice except two numbers. Find them.

```python
def two_single_numbers(nums):
    xor = 0
    for num in nums:
        xor ^= num

    # Rightmost set bit
    rightmost_bit = xor & -xor

    x = y = 0
    for num in nums:
        if num & rightmost_bit:
            x ^= num
        else:
            y ^= num
    return x, y

# Test
print(two_single_numbers([2, 4, 7, 9, 2, 4]))  # (7, 9)
```

🧠 **Explanation**:
First XOR gives `a ^ b`. Then we split the array based on a differing bit.

---

### **2. Find XOR of All Subsets of an Array**

**Problem**: Given an array, return the XOR of all possible subset XORs.

```python
def subset_xor_sum(nums):
    total = 0
    n = len(nums)
    for i in range(1 << n):
        subset_xor = 0
        for j in range(n):
            if i & (1 << j):
                subset_xor ^= nums[j]
        total += subset_xor
    return total

# Test
print(subset_xor_sum([1, 3]))  # 6
```

🧠 **Explanation**:
Loop over all subsets using bitmasking. For each mask, include elements where the j-th bit is set.

---

### **3. Count Total Set Bits from 1 to N**

```python
def count_total_set_bits(n):
    count = 0
    i = 0
    while (1 << i) <= n:
        total_pairs = n + 1
        count += (total_pairs // (1 << (i + 1))) * (1 << i)
        count += max(0, (total_pairs % (1 << (i + 1)) - (1 << i)))
        i += 1
    return count

# Test
print(count_total_set_bits(7))  # 12
```

🧠 **Explanation**:
Efficient method based on how many times each bit position contributes a `1`.

---

### **4. Subsets Using Bitmasking**

```python
def generate_subsets(nums):
    n = len(nums)
    subsets = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        subsets.append(subset)
    return subsets

# Test
print(generate_subsets([1, 2]))
```

🧠 **Explanation**:
`2^n` masks → each represents a subset.

---

### **5. Find the Missing Number**

**Problem**: Find the missing number in `[0, 1, ..., n]` with one number missing.

```python
def find_missing(nums):
    n = len(nums)
    xor = 0
    for i in range(n + 1):
        xor ^= i
    for num in nums:
        xor ^= num
    return xor

# Test
print(find_missing([0, 1, 3]))  # 2
```

🧠 **Explanation**:
XOR of full range ^ array gives the missing number.

---

### **6. Gray Code Generation**

```python
def gray_code(n):
    result = []
    for i in range(1 << n):
        result.append(i ^ (i >> 1))
    return result

# Test
print(gray_code(2))  # [0, 1, 3, 2]
```

🧠 **Explanation**:
Gray code of `n` bits: `i ^ (i >> 1)` ensures only one bit changes at a time.

---

### **7. Bitwise AND of Numbers in a Range**

```python
def range_bitwise_and(left, right):
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift

# Test
print(range_bitwise_and(5, 7))  # 4
```

🧠 **Explanation**:
Keep right-shifting until both numbers are the same, then shift back.

---

### **8. Reverse Bits of a 32-bit Integer**

```python
def reverse_bits(n):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        result |= bit << (31 - i)
    return result

# Test
print(reverse_bits(0b00000010100101000001111010011100))  # Output: 964176192
```

🧠 **Explanation**:
For each bit position, copy it in reverse order.

---

### **9. Add Two Numbers Without `+` or `-`**

```python
def add(a, b):
    MAX = 0xFFFFFFFF
    while b != 0:
        carry = (a & b) & MAX
        a = (a ^ b) & MAX
        b = (carry << 1) & MAX
    return a if a <= 0x7FFFFFFF else ~(a ^ MAX)

# Test
print(add(5, 3))  # 8
```

🧠 **Explanation**:
Use XOR for sum and AND+shift for carry, loop until carry is 0.

---

### **10. Find the Position of the Only Set Bit**

**Problem**: If a number has only one set bit (e.g., 8 → `0b1000`), return its position.

```python
def find_position(n):
    if n == 0 or (n & (n - 1)) != 0:
        return -1  # not power of 2
    pos = 1
    while n > 1:
        n >>= 1
        pos += 1
    return pos

# Test
print(find_position(16))  # 5
```

🧠 **Explanation**:
Count how many right shifts are needed until we reach 1.

---

Would you like **advanced-level** bit manipulation problems next (e.g., bitmask DP, max XOR pair, trie with bits, etc.)?
