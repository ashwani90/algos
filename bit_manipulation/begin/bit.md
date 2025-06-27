Here are **10 beginner-level Bit Manipulation problems** along with detailed **Python solutions and explanations**. These are great to get familiar with bitwise operators like `AND (&)`, `OR (|)`, `XOR (^)`, `NOT (~)`, left shift `<<`, and right shift `>>`.

---

### **1. Check if a Number is Even or Odd**

**Problem**: Given a number `n`, determine whether it is even or odd.

```python
def is_even(n):
    return (n & 1) == 0

# Test
print(is_even(4))  # True (even)
print(is_even(7))  # False (odd)
```

🧠 **Explanation**:
If the last bit of a number is `0`, the number is even. We use `n & 1` to check the last bit.

---

### **2. Check if a Number is a Power of Two**

**Problem**: Return `True` if `n` is a power of two, else `False`.

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Test
print(is_power_of_two(8))   # True
print(is_power_of_two(10))  # False
```

🧠 **Explanation**:
Powers of two have only one set bit in binary. `n & (n-1)` removes the lowest set bit. If the result is 0, `n` was a power of two.

---

### **3. Count the Number of Set Bits in an Integer**

**Problem**: Count the number of 1's in the binary representation of `n`.

```python
def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)  # removes the lowest set bit
        count += 1
    return count

# Test
print(count_set_bits(13))  # 3 (1101)
```

🧠 **Explanation**:
Each `n & (n-1)` removes one `1` from binary representation.

---

### **4. Find the Only Non-Repeating Element in an Array**

**Problem**: Every element appears twice except one. Find it.

```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test
print(single_number([2, 3, 2, 3, 4]))  # 4
```

🧠 **Explanation**:
XOR of a number with itself is 0, and XOR with 0 is the number. All duplicates cancel out.

---

### **5. Get the Rightmost Set Bit of a Number**

**Problem**: Return the rightmost set bit of `n`.

```python
def rightmost_set_bit(n):
    return n & -n

# Test
print(bin(rightmost_set_bit(10)))  # 0b10
```

🧠 **Explanation**:
`n & -n` isolates the lowest set bit using two's complement.

---

### **6. Turn Off the Rightmost Set Bit**

**Problem**: Given a number `n`, turn off the rightmost set bit.

```python
def turn_off_rightmost_set_bit(n):
    return n & (n - 1)

# Test
print(bin(turn_off_rightmost_set_bit(10)))  # 0b1000
```

🧠 **Explanation**:
`n & (n-1)` removes the lowest set bit.

---

### **7. Check if kth Bit is Set**

**Problem**: Given `n` and `k`, check if the k-th bit is set (0-indexed from right).

```python
def is_kth_bit_set(n, k):
    return (n & (1 << k)) != 0

# Test
print(is_kth_bit_set(10, 1))  # True (1010)
print(is_kth_bit_set(10, 2))  # False
```

🧠 **Explanation**:
Shift 1 to the `k`-th position and `AND` it with `n`.

---

### **8. Swap Two Numbers Without a Temp Variable**

```python
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

# Test
print(swap(5, 7))  # (7, 5)
```

🧠 **Explanation**:
Bitwise XOR trick swaps values without a temporary variable.

---

### **9. Multiply an Integer by 2 Using Bitwise Operator**

```python
def multiply_by_2(n):
    return n << 1

# Test
print(multiply_by_2(5))  # 10
```

🧠 **Explanation**:
Left shift `n` by 1 bit → multiplies by 2.

---

### **10. Divide an Integer by 2 Using Bitwise Operator**

```python
def divide_by_2(n):
    return n >> 1

# Test
print(divide_by_2(8))  # 4
```

🧠 **Explanation**:
Right shift `n` by 1 bit → divides by 2.

---

Would you like 10 **intermediate-level** bit manipulation problems next (like finding 2 non-repeating elements, subset generation using bits, or bitmask DP)?
