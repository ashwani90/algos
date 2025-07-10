Here are **10 beginner-level number theory problems** along with their **Python solutions and detailed explanations**. These problems cover fundamental concepts such as **divisibility, prime numbers, GCD/LCM, modular arithmetic, and basic properties of numbers**.

---

## ✅ 10 Beginner Number Theory Problems

---

### **1. Check if a number is prime**

**Problem:**
Determine whether a number `n` is prime.

```python
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))  # Output: True
```

**Explanation:**
A prime number has no divisors other than 1 and itself. We only check up to √n for efficiency.

---

### **2. Compute GCD (Greatest Common Divisor)**

**Problem:**
Find the GCD of two integers `a` and `b`.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(36, 60))  # Output: 12
```

**Explanation:**
Uses the **Euclidean algorithm**. Repeatedly replace `(a, b)` with `(b, a % b)`.

---

### **3. Compute LCM (Least Common Multiple)**

**Problem:**
Find the LCM of two numbers using GCD.

```python
def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(4, 6))  # Output: 12
```

**Explanation:**
LCM is calculated using the formula: `LCM(a, b) = (a × b) / GCD(a, b)`.

---

### **4. Count digits of a number**

**Problem:**
Count the number of digits in a positive integer.

```python
def count_digits(n):
    return len(str(n))

print(count_digits(12345))  # Output: 5
```

**Explanation:**
Convert number to string and count characters.

---

### **5. Reverse digits of a number**

**Problem:**
Reverse the digits of a number `n`.

```python
def reverse_number(n):
    return int(str(n)[::-1])

print(reverse_number(123))  # Output: 321
```

**Explanation:**
Convert to string, reverse it, and convert back.

---

### **6. Check if a number is a palindrome**

**Problem:**
Check whether `n` reads the same forward and backward.

```python
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(121))  # Output: True
```

**Explanation:**
Compares the string with its reverse.

---

### **7. Sum of digits of a number**

**Problem:**
Compute the sum of the digits of `n`.

```python
def sum_of_digits(n):
    return sum(int(d) for d in str(n))

print(sum_of_digits(1234))  # Output: 10
```

**Explanation:**
Convert to string, iterate over digits, and sum.

---

### **8. Find all divisors of a number**

**Problem:**
Return all positive integers that divide `n`.

```python
def divisors(n):
    result = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)

print(divisors(28))  # Output: [1, 2, 4, 7, 14, 28]
```

**Explanation:**
Checks divisors up to √n and adds both `i` and `n//i`.

---

### **9. Count number of primes ≤ n (Sieve of Eratosthenes)**

**Problem:**
Count all prime numbers up to `n`.

```python
def count_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return sum(is_prime)

print(count_primes(10))  # Output: 4 (2, 3, 5, 7)
```

**Explanation:**
Sieve marks non-primes in a boolean array up to `n`.

---

### **10. Compute power with modular arithmetic**

**Problem:**
Compute `(a^b) % mod` efficiently.

```python
def mod_pow(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result

print(mod_pow(2, 10, 1000))  # Output: 24
```

**Explanation:**
This uses **binary exponentiation** to reduce time from O(b) to O(log b).

---

Would you like intermediate number theory problems next (like Euler’s totient, modular inverse, prime factorization, etc.)?
