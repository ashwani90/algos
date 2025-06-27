Sure! Here are **10 beginner-level combinatorics problems** along with their **solutions and explanations** in Python:

---

### 1. **Calculate nCr (Binomial Coefficient)**

**Problem:**
Calculate the number of ways to choose `r` items from `n` items (nCr).

**Solution:**

```python
def nCr(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    # Use Pascal's rule: nCr = (n-1)C(r-1) + (n-1)Cr
    return nCr(n-1, r-1) + nCr(n-1, r)

print(nCr(5, 2))  # Output: 10
```

**Explanation:**
The binomial coefficient can be computed recursively using Pascal’s rule. Base cases are when r=0 or r=n.

---

### 2. **Factorial Calculation**

**Problem:**
Calculate factorial of a number n.

**Solution:**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120
```

**Explanation:**
Factorial of n (n!) is the product of all positive integers up to n.

---

### 3. **Number of Permutations (nPr)**

**Problem:**
Calculate number of permutations of `r` items from `n` items (nPr).

**Solution:**

```python
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def nPr(n, r):
    return factorial(n) // factorial(n-r)

print(nPr(5, 3))  # Output: 60
```

**Explanation:**
Number of permutations nPr = n! / (n-r)!

---

### 4. **Count Number of Ways to Arrange 3 Different Balls in 2 Boxes**

**Problem:**
How many ways can you put 3 different balls into 2 boxes, where boxes can be empty?

**Solution:**

Each ball has 2 choices (box1 or box2):

```python
ways = 2 ** 3
print(ways)  # Output: 8
```

**Explanation:**
Each ball can go to any of the two boxes independently. So total ways = 2^3.

---

### 5. **Calculate the Number of Subsets of a Set**

**Problem:**
Find the total number of subsets of a set with n elements.

**Solution:**

```python
def subsets_count(n):
    return 2 ** n

print(subsets_count(4))  # Output: 16
```

**Explanation:**
Each element can either be included or excluded, so total subsets = 2^n.

---

### 6. **Find the Number of Ways to Distribute k Identical Balls into n Different Boxes**

**Problem:**
Number of ways to distribute k identical balls into n distinct boxes.

**Solution:** (Using stars and bars theorem)

```python
def nCr(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)

def ways_to_distribute(k, n):
    # Number of non-negative integer solutions to x1 + x2 + ... + xn = k
    return nCr(k + n -1, n -1)

print(ways_to_distribute(3, 2))  # Output: 4
```

**Explanation:**
This is a classic stars and bars problem where balls are identical and boxes distinct.

---

### 7. **Count Number of Ways to Arrange n People in a Circle**

**Problem:**
Number of ways to seat n distinct people around a circular table.

**Solution:**

```python
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def circular_permutations(n):
    if n == 0:
        return 0
    return factorial(n-1)

print(circular_permutations(4))  # Output: 6
```

**Explanation:**
Circular permutations = (n-1)! because rotations are considered the same arrangement.

---

### 8. **Count Number of Ways to Select 2 Items from 5 (Combination)**

**Problem:**
Select 2 items from 5 items.

**Solution:**

```python
def nCr(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)

print(nCr(5, 2))  # Output: 10
```

**Explanation:**
Uses the binomial coefficient formula for combinations.

---

### 9. **Count Number of Ways to Arrange 3 Identical Balls in a Row**

**Problem:**
Arrange 3 identical balls in a row — how many distinct arrangements?

**Solution:**

Since balls are identical, there is only 1 way.

```python
print(1)
```

**Explanation:**
Identical items have only one arrangement as swapping does not change the order.

---

### 10. **Number of Ways to Select k Items From n Items With Repetition Allowed**

**Problem:**
How many ways to select k items from n items with repetition?

**Solution:**
Equivalent to stars and bars problem.

```python
def nCr(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)

def combinations_with_repetition(n, k):
    return nCr(n + k - 1, k)

print(combinations_with_repetition(3, 2))  # Output: 6
```

**Explanation:**
When repetition is allowed, the formula is C(n+k-1, k).

---

If you'd like, I can provide intermediate or advanced combinatorics problems next! Would you like that?
