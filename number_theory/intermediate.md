Here are **10 intermediate-level number theory problems** with detailed Python solutions and explanations. These problems introduce concepts like **prime factorization, modular inverses, Euler’s totient function, Chinese remainder theorem, and more** — great for building a solid foundation beyond beginner topics.

---

## ✅ 10 Intermediate Number Theory Problems

---

### **1. Prime Factorization**

**Problem:**
Find the prime factors of a number `n`.

```python
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(84))  # Output: [2, 2, 3, 7]
```

**Explanation:**
Divide by 2 repeatedly, then test odd factors up to √n.

---

### **2. Count Divisors Using Prime Factorization**

**Problem:**
Find the number of divisors of `n`.

```python
from collections import Counter

def count_divisors(n):
    factors = prime_factors(n)
    c = Counter(factors)
    count = 1
    for exp in c.values():
        count *= (exp + 1)
    return count

print(count_divisors(28))  # Output: 6
```

**Explanation:**
If prime factorization is $p_1^{e_1} \times p_2^{e_2} \cdots$, number of divisors = $\prod (e_i + 1)$.

---

### **3. Euler’s Totient Function**

**Problem:**
Calculate $\varphi(n)$, number of integers ≤ n that are coprime to n.

```python
def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1 if p == 2 else 2
    if n > 1:
        result -= result // n
    return result

print(euler_totient(9))  # Output: 6
```

**Explanation:**
Uses the formula $\varphi(n) = n \times \prod_{p|n}(1 - \frac{1}{p})$ where p are prime factors.

---

### **4. Modular Inverse (using Extended Euclidean Algorithm)**

**Problem:**
Find modular inverse of `a` under modulo `m`.

```python
def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist if gcd != 1
    return x % m

print(mod_inverse(3, 11))  # Output: 4
```

**Explanation:**
Modular inverse exists only if `a` and `m` are coprime.

---

### **5. Chinese Remainder Theorem**

**Problem:**
Solve system:

$$
x \equiv a_1 \mod m_1 \\
x \equiv a_2 \mod m_2
$$

```python
def crt(a1, m1, a2, m2):
    gcd, x, y = extended_gcd(m1, m2)
    if (a2 - a1) % gcd != 0:
        return None
    lcm = (m1 * m2) // gcd
    x0 = (a1 + (a2 - a1) // gcd * x * m1) % lcm
    return x0 if x0 >= 0 else x0 + lcm

print(crt(2, 3, 3, 5))  # Output: 8
```

**Explanation:**
Find solution to simultaneous congruences using Extended Euclidean Algorithm.

---

### **6. Check if a Number is a Perfect Square**

```python
def is_perfect_square(n):
    root = int(n**0.5)
    return root * root == n

print(is_perfect_square(49))  # Output: True
```

**Explanation:**
Compare square of floor of sqrt with n.

---

### **7. Number of trailing zeros in n!**

**Problem:**
Count how many zeros at the end of factorial of `n`.

```python
def trailing_zeros(n):
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count

print(trailing_zeros(100))  # Output: 24
```

**Explanation:**
Trailing zeros come from factors of 10 → pairs of 2 and 5, 5’s are limiting factor.

---

### **8. Check if a number is a power of two**

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(16))  # Output: True
```

**Explanation:**
Only powers of two have a single set bit.

---

### **9. Sum of all divisors of n**

```python
from collections import Counter

def sum_of_divisors(n):
    factors = prime_factors(n)
    c = Counter(factors)
    total = 1
    for p, e in c.items():
        total *= (p**(e+1) - 1) // (p - 1)
    return total

print(sum_of_divisors(6))  # Output: 12 (1+2+3+6)
```

**Explanation:**
Formula: sum of divisors = $\prod \frac{p^{e+1}-1}{p-1}$

---

### **10. Find the highest power of prime p dividing n!**

```python
def highest_power(n, p):
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count

print(highest_power(10, 2))  # Output: 8 (power of 2 in 10!)
```

**Explanation:**
Count multiples of p, p², p³,... to find exponent of p in factorial.

---

If you want, I can now provide **solutions and explanations for advanced number theory problems** like primality testing (Miller-Rabin), discrete logarithms, or fast exponentiation tricks!
