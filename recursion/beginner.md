Absolutely! Here are **10 beginner-level recursion problems** with detailed solutions and explanations in Python.

---

### 1. **Print numbers from 1 to n**

**Problem:**
Print numbers from 1 to n using recursion.

**Solution:**

```python
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n)

print_numbers(5)
```

**Explanation:**
The function calls itself with `n-1` until it reaches 0 (base case), then prints numbers on the way back (unwinding recursion).

---

### 2. **Calculate factorial of a number**

**Problem:**
Calculate `n!` recursively.

**Solution:**

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120
```

**Explanation:**
Factorial of `n` is `n * factorial(n-1)`. Base case is factorial of 0 equals 1.

---

### 3. **Sum of digits of a number**

**Problem:**
Find sum of digits of a positive integer.

**Solution:**

```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))  # Output: 10
```

**Explanation:**
Add last digit (`n%10`) plus sum of digits of remaining number (`n//10`).

---

### 4. **Check if a string is palindrome**

**Problem:**
Check if a given string is a palindrome recursively.

**Solution:**

```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

**Explanation:**
Compare first and last characters; if equal, check the substring inside recursively.

---

### 5. **Calculate nth Fibonacci number**

**Problem:**
Find the nth Fibonacci number recursively.

**Solution:**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8
```

**Explanation:**
Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2), base cases for 0 and 1.

---

### 6. **Print array elements recursively**

**Problem:**
Print all elements of an array recursively.

**Solution:**

```python
def print_array(arr, index=0):
    if index == len(arr):
        return
    print(arr[index])
    print_array(arr, index+1)

print_array([10, 20, 30, 40])
```

**Explanation:**
Print element at current index, then call recursively with next index.

---

### 7. **Count number of digits in a number**

**Problem:**
Count digits in a positive integer using recursion.

**Solution:**

```python
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(12345))  # Output: 5
```

**Explanation:**
Each recursive call strips one digit; sum counts the total digits.

---

### 8. **Find power of a number**

**Problem:**
Compute `x^n` (x to the power n) recursively.

**Solution:**

```python
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

print(power(2, 5))  # Output: 32
```

**Explanation:**
Multiply `x` by the result of `x^(n-1)` recursively.

---

### 9. **Reverse a string recursively**

**Problem:**
Return the reverse of a string using recursion.

**Solution:**

```python
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # Output: "olleh"
```

**Explanation:**
Recursively reverse substring excluding first character and append first character at the end.

---

### 10. **Find GCD of two numbers**

**Problem:**
Find Greatest Common Divisor (GCD) of two numbers using recursion.

**Solution:**

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  # Output: 6
```

**Explanation:**
Use Euclid’s algorithm: GCD(a, b) = GCD(b, a mod b), base case when b = 0.

---

If you'd like, I can provide more examples or explain any problem in further detail!
