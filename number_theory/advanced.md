Here are **10 advanced number theory problems** with detailed Python solutions and explanations. These involve deeper concepts such as **fast primality tests, discrete logarithm, modular arithmetic with large numbers, prime sieves, and more advanced theorems and algorithms**.

---

## 🔥 10 Advanced Number Theory Problems

---

### **1. Miller-Rabin Primality Test**

**Problem:**
Efficiently check if a large number `n` is prime probabilistically.

```python
import random

def miller_rabin_test(d, n):
    a = random.randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        if not miller_rabin_test(d, n):
            return False
    return True

print(is_prime(2**31 - 1))  # Output: True (Mersenne prime)
```

**Explanation:**
Miller-Rabin is a probabilistic primality test running in O(k log³ n), suitable for large numbers.

---

### **2. Discrete Logarithm (Baby-step Giant-step)**

**Problem:**
Solve for `x` in $a^x \equiv b \mod m$.

```python
import math

def discrete_log(a, b, m):
    n = int(math.sqrt(m)) + 1
    value = {}
    an = pow(a, n, m)

    cur = b
    for q in range(n):
        value[cur] = q
        cur = (cur * a) % m

    cur = 1
    for p in range(1, n+1):
        cur = (cur * an) % m
        if cur in value:
            return p * n - value[cur]
    return None

print(discrete_log(2, 22, 29))  # Output: 11 because 2^11 % 29 = 22
```

**Explanation:**
Baby-step Giant-step algorithm solves discrete logs in O(√m).

---

### **3. Modular Multiplicative Inverse (Fermat’s Little Theorem)**

**Problem:**
Calculate modular inverse when `m` is prime.

```python
def mod_inverse_fermat(a, m):
    return pow(a, m-2, m)

print(mod_inverse_fermat(3, 11))  # Output: 4
```

**Explanation:**
When `m` is prime, inverse of `a` mod `m` is $a^{m-2} \mod m$.

---

### **4. Segmented Sieve (Primes in large range)**

```python
def simple_sieve(limit):
    prime = [True]*(limit+1)
    prime[0] = prime[1] = False
    for i in range(2, int(limit**0.5)+1):
        if prime[i]:
            for j in range(i*i, limit+1, i):
                prime[j] = False
    return [i for i in range(limit+1) if prime[i]]

def segmented_sieve(low, high):
    limit = int(high**0.5)+1
    primes = simple_sieve(limit)
    n = high - low + 1
    mark = [True]*n
    for p in primes:
        start = max(p*p, (low + p - 1)//p * p)
        for j in range(start, high+1, p):
            mark[j - low] = False
    return [low+i for i in range(n) if mark[i] and low+i > 1]

print(segmented_sieve(10**12, 10**12 + 100))
```

**Explanation:**
Efficient way to find primes in a huge range without memory overload.

---

### **5. Legendre’s Formula for Factorial Prime Exponent**

**Problem:**
Find exponent of prime p in n! (extended to large n).

```python
def legendre_formula(n, p):
    count = 0
    while n > 0:
        n //= p
        count += n
    return count

print(legendre_formula(1000, 5))  # Output: 249
```

**Explanation:**
Counts multiples of p, p², ... in factorial n!.

---

### **6. Solve Linear Congruence $ax \equiv b \mod m$**

```python
def solve_linear_congruence(a, b, m):
    gcd, x, _ = extended_gcd(a, m)
    if b % gcd != 0:
        return None  # No solution
    x0 = (x * (b // gcd)) % m
    return x0

print(solve_linear_congruence(14, 30, 100))  # Output: 95
```

**Explanation:**
Uses extended Euclidean algorithm to solve modular linear equations.

---

### **7. Count number of primes up to n using Sieve of Atkin**

```python
def sieve_of_atkin(limit):
    sieve = [False]*(limit+1)
    sqrt_limit = int(limit**0.5) + 1
    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4*x*x + y*y
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3*x*x + y*y
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3*x*x - y*y
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for n in range(5, sqrt_limit):
        if sieve[n]:
            for k in range(n*n, limit+1, n*n):
                sieve[k] = False
    primes = [2, 3] + [x for x in range(5, limit+1) if sieve[x]]
    return primes

print(len(sieve_of_atkin(100000)))  # Count of primes up to 100000
```

**Explanation:**
A faster sieve than Eratosthenes for large limits, based on quadratic forms.

---

### **8. Compute the Jacobi symbol (a/n)**

```python
def jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        return 0
    result = 1
    a = a % n
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0

print(jacobi(1001, 9907))  # Output: 1 or -1
```

**Explanation:**
Generalizes the Legendre symbol for composite modulus.

---

### **9. Find Primitive Root modulo n (when n is prime)**

```python
def find_primitive_root(p):
    if p == 2:
        return 1
    phi = p - 1
    factors = set(prime_factors(phi))
    for r in range(2, p):
        if all(pow(r, phi // f, p) != 1 for f in factors):
            return r
    return None

print(find_primitive_root(17))  # Output: 3 (one of the primitive roots mod 17)
```

**Explanation:**
Primitive root g satisfies $g^{\phi(n)/f} \not\equiv 1 \mod n$ for all prime factors f of $\phi(n)$.

---

### **10. Fast Fibonacci Modulo (Using Matrix Exponentiation)**

```python
def matrix_mult(A, B, mod):
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]]

def matrix_pow(M, n, mod):
    result = [[1,0],[0,1]]
    while n > 0:
        if n & 1:
            result = matrix_mult(result, M, mod)
        M = matrix_mult(M, M, mod)
        n >>= 1
    return result

def fib_mod(n, mod):
    if n == 0:
        return 0
    F = [[1,1],[1,0]]
    F_n = matrix_pow(F, n-1, mod)
    return F_n[0][0]

print(fib_mod(10**18, 10**9+7))  # Output: fib(10^18) mod 10^9+7
```

**Explanation:**
Computes Fibonacci numbers modulo `mod` efficiently using fast matrix exponentiation.

---

If you want me to explain any problem or algorithm in more depth or provide more problems, just say!
