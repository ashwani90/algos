Sure! Here are **10 beginner-level bitmask problems** with detailed solutions and explanations in Python:

---

### 1. **Check if a Number is a Power of Two**

**Problem:**
Determine if a given integer `n` is a power of two.

**Solution:**

```python
def is_power_of_two(n):
    # A number n is a power of two if it has exactly one bit set
    # n & (n-1) clears the lowest set bit; if result is zero and n > 0, then true
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(16))  # True
print(is_power_of_two(18))  # False
```

**Explanation:**
Powers of two in binary look like 1000... only one bit set. Subtracting 1 flips all lower bits, so `n & (n-1)` is zero only for powers of two.

---

### 2. **Count the Number of Set Bits in an Integer**

**Problem:**
Count how many 1s are in the binary representation of an integer.

**Solution:**

```python
def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)  # Remove lowest set bit
        count += 1
    return count

print(count_set_bits(13))  # 3 (1101)
```

**Explanation:**
Each `n &= n-1` removes the lowest set bit, so counting iterations counts 1 bits efficiently.

---

### 3. **Check if Two Integers have Opposite Signs**

**Problem:**
Determine if two integers have opposite signs using bit operations.

**Solution:**

```python
def opposite_signs(x, y):
    # The sign bit is different if x ^ y has its highest bit set (negative number)
    return (x ^ y) < 0

print(opposite_signs(4, -5))  # True
print(opposite_signs(-4, -5)) # False
```

**Explanation:**
XOR flips bits where signs differ. Negative result means sign bits differ.

---

### 4. **Toggle the k-th Bit of a Number**

**Problem:**
Toggle (flip) the k-th bit of an integer `n`.

**Solution:**

```python
def toggle_kth_bit(n, k):
    return n ^ (1 << k)

print(bin(toggle_kth_bit(10, 1)))  # Toggle bit 1 in 1010 => 1000 (8)
```

**Explanation:**
XOR with `1 << k` flips the k-th bit.

---

### 5. **Check if k-th Bit is Set**

**Problem:**
Check if the k-th bit (0-indexed from right) in integer `n` is 1.

**Solution:**

```python
def is_kth_bit_set(n, k):
    return (n & (1 << k)) != 0

print(is_kth_bit_set(10, 1))  # True (10 is 1010 binary)
print(is_kth_bit_set(10, 2))  # False
```

**Explanation:**
AND with mask isolates bit; if non-zero, bit is set.

---

### 6. **Set the k-th Bit of a Number**

**Problem:**
Set the k-th bit of an integer `n` to 1.

**Solution:**

```python
def set_kth_bit(n, k):
    return n | (1 << k)

print(bin(set_kth_bit(8, 1)))  # Set bit 1 in 1000 => 1010 (10)
```

**Explanation:**
OR with mask sets the bit to 1.

---

### 7. **Clear the k-th Bit of a Number**

**Problem:**
Clear (set to 0) the k-th bit of an integer `n`.

**Solution:**

```python
def clear_kth_bit(n, k):
    return n & ~(1 << k)

print(bin(clear_kth_bit(10, 1)))  # Clear bit 1 in 1010 => 1000 (8)
```

**Explanation:**
AND with inverse mask clears bit.

---

### 8. **Find the Lowest Set Bit**

**Problem:**
Get the value of the lowest set bit of integer `n`.

**Solution:**

```python
def lowest_set_bit(n):
    return n & (-n)

print(bin(lowest_set_bit(12)))  # 4 (1100 & 0100)
```

**Explanation:**
Two's complement `-n` flips bits and adds 1; AND isolates lowest set bit.

---

### 9. **Count Number of Bits to Flip to Convert A to B**

**Problem:**
Count how many bits differ between two integers A and B.

**Solution:**

```python
def bits_to_flip(a, b):
    xor = a ^ b
    count = 0
    while xor:
        xor &= xor - 1
        count += 1
    return count

print(bits_to_flip(10, 15))  # 2
```

**Explanation:**
XOR highlights differing bits; count set bits in XOR.

---

### 10. **Check if a Number is Even or Odd Using Bitmask**

**Problem:**
Check if a number is even or odd using bit operations.

**Solution:**

```python
def is_odd(n):
    return (n & 1) == 1

print(is_odd(10))  # False
print(is_odd(15))  # True
```

**Explanation:**
Least significant bit 1 means odd number.

---

If you want me to provide intermediate or advanced bitmask problems next, just say!
