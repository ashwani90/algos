Sure! Here are **10 beginner-level Binary Indexed Tree (Fenwick Tree) problems** with their solutions and explanations in Python.

---

### What is a Binary Indexed Tree (Fenwick Tree)?

A **Binary Indexed Tree** helps efficiently compute prefix sums and update elements in a list in **O(log n)** time. It's useful for queries like "sum of first k elements" and "update element at position i."

---

## 1. Fenwick Tree: Build and Basic Query (Prefix Sum)

**Problem:**
Given an array, build a Fenwick Tree and find the prefix sum up to index `i`.

**Solution:**

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

arr = [1, 2, 3, 4, 5]
ft = FenwickTree(len(arr))
for idx, val in enumerate(arr, 1):
    ft.update(idx, val)

print(ft.prefix_sum(3))  # sum of arr[0..2] = 1+2+3 = 6
```

**Explanation:**

* `update(i, delta)` adds `delta` to position `i` and all relevant ancestors.
* `prefix_sum(i)` computes sum from `1` to `i` by moving downwards.

---

## 2. Range Sum Query using Fenwick Tree

**Problem:**
Find the sum of elements between indices `l` and `r`.

**Solution:**

```python
def range_sum(ft, l, r):
    return ft.prefix_sum(r) - ft.prefix_sum(l - 1)

print(range_sum(ft, 2, 4))  # sum arr[1..3] = 2+3+4=9
```

**Explanation:**
Use prefix sums: sum(l to r) = prefix\_sum(r) - prefix\_sum(l-1).

---

## 3. Update Value in Array and Fenwick Tree

**Problem:**
Update value at index `i` to `new_val` and reflect it in Fenwick Tree.

**Solution:**

```python
def update_value(arr, ft, i, new_val):
    delta = new_val - arr[i-1]
    arr[i-1] = new_val
    ft.update(i, delta)

update_value(arr, ft, 3, 10)  # arr[2] = 10
print(ft.prefix_sum(5))  # sum is now 1+2+10+4+5=22
```

**Explanation:**
Calculate change `delta` and update Fenwick Tree.

---

## 4. Count Frequency of Elements (Fenwick Tree as Frequency Table)

**Problem:**
Given values between 1 and max\_val, count frequency of each value dynamically.

**Solution:**

```python
max_val = 10
freq_tree = FenwickTree(max_val)

def add_freq(x):
    freq_tree.update(x, 1)

def get_freq(x):
    return freq_tree.prefix_sum(x) - freq_tree.prefix_sum(x-1)

# Add frequencies
add_freq(3)
add_freq(3)
add_freq(5)
print(get_freq(3))  # Output: 2
print(freq_tree.prefix_sum(5))  # frequency of <=5: 3
```

**Explanation:**
Fenwick Tree used to store frequency counts and prefix sums.

---

## 5. Number of Smaller Elements to the Left

**Problem:**
For each element, count how many elements before it are smaller.

**Solution:**

```python
def smaller_to_left(arr):
    max_val = max(arr)
    ft = FenwickTree(max_val)
    result = []
    for x in arr:
        result.append(ft.prefix_sum(x - 1))
        ft.update(x, 1)
    return result

print(smaller_to_left([3, 4, 1, 2]))  # Output: [0,1,0,1]
```

**Explanation:**
For each element `x`, prefix\_sum(x-1) counts smaller elements seen so far.

---

## 6. Number of Greater Elements to the Right

**Problem:**
Count how many elements to the right are greater.

**Solution:**

```python
def greater_to_right(arr):
    max_val = max(arr)
    ft = FenwickTree(max_val)
    result = [0] * len(arr)
    for i in reversed(range(len(arr))):
        x = arr[i]
        result[i] = ft.prefix_sum(max_val) - ft.prefix_sum(x)
        ft.update(x, 1)
    return result

print(greater_to_right([3, 4, 1, 2]))  # Output: [1,0,2,0]
```

**Explanation:**
We process from right to left and use prefix sums to count greater elements.

---

## 7. Find Inversion Count in Array

**Problem:**
Count the number of inversions (pairs `i < j` and `arr[i] > arr[j]`).

**Solution:**

```python
def inversion_count(arr):
    max_val = max(arr)
    ft = FenwickTree(max_val)
    inv_count = 0
    for i in reversed(range(len(arr))):
        inv_count += ft.prefix_sum(arr[i] - 1)
        ft.update(arr[i], 1)
    return inv_count

print(inversion_count([8, 4, 2, 1]))  # Output: 6
```

**Explanation:**
Count how many smaller elements to the right by prefix sums.

---

## 8. Find kth Smallest Element using Fenwick Tree

**Problem:**
Given frequencies stored in Fenwick Tree, find the k-th smallest number.

**Solution:**

```python
def find_kth(ft, k):
    pos = 0
    bit_mask = 1 << (ft.n.bit_length())  # largest power of 2 ≤ n

    while bit_mask > 0:
        next_pos = pos + bit_mask
        if next_pos <= ft.n and ft.tree[next_pos] < k:
            k -= ft.tree[next_pos]
            pos = next_pos
        bit_mask >>= 1
    return pos + 1

freq_tree = FenwickTree(10)
freq_tree.update(1, 1)
freq_tree.update(2, 2)
freq_tree.update(5, 3)
print(find_kth(freq_tree, 4))  # Output: 2 (4th smallest element)
```

**Explanation:**
Use binary lifting on Fenwick Tree to find index where cumulative frequency reaches `k`.

---

## 9. Fenwick Tree for XOR Prefix Queries

**Problem:**
Implement Fenwick Tree to handle XOR queries (prefix XOR).

**Solution:**

```python
class FenwickTreeXOR:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] ^= val
            i += i & -i

    def prefix_xor(self, i):
        result = 0
        while i > 0:
            result ^= self.tree[i]
            i -= i & -i
        return result

arr = [3, 2, 4, 5, 1]
ft = FenwickTreeXOR(len(arr))
for idx, val in enumerate(arr, 1):
    ft.update(idx, val)

print(ft.prefix_xor(3))  # XOR of first 3 elements = 3 ^ 2 ^ 4 = 5
```

**Explanation:**
Fenwick Tree also works with XOR operation replacing sum and add.

---

## 10. Find Number of Elements Less Than or Equal to X in Dynamic Stream

**Problem:**
Maintain dynamic elements, query count of numbers ≤ X at any time.

**Solution:**

```python
max_val = 1000
ft = FenwickTree(max_val)

def add_num(x):
    ft.update(x, 1)

def count_less_equal(x):
    return ft.prefix_sum(x)

add_num(5)
add_num(3)
add_num(8)
print(count_less_equal(5))  # Output: 2 (elements ≤ 5)
```

**Explanation:**
Fenwick Tree stores frequencies; prefix sums give counts ≤ X efficiently.

---

---

If you want, I can explain any problem more deeply or give you more problems. Would you like that?
