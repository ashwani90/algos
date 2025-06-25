Sure! Here are **10 beginner-level string problems** with their **solutions and explanations** in Python.

---

### 1. **Reverse a String**

**Problem:** Given a string, reverse it.

**Solution:**

```python
def reverse_string(s: str) -> str:
    return s[::-1]

# Example
print(reverse_string("hello"))  # Output: "olleh"
```

**Explanation:**
Slicing `s[::-1]` creates a reversed copy of the string. This is the simplest and most pythonic way to reverse a string.

---

### 2. **Check Palindrome**

**Problem:** Check if a string is a palindrome (reads same forwards and backwards).

**Solution:**

```python
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Example
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

**Explanation:**
If the string equals its reverse, it is a palindrome.

---

### 3. **Count Vowels in a String**

**Problem:** Count the number of vowels (a, e, i, o, u) in a string.

**Solution:**

```python
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example
print(count_vowels("Hello World"))  # Output: 3
```

**Explanation:**
We iterate through each character and increment the count if it's a vowel.

---

### 4. **Find First Non-Repeating Character**

**Problem:** Find the first character in a string that does not repeat.

**Solution:**

```python
from collections import Counter

def first_non_repeating_char(s: str) -> str:
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char
    return ""

# Example
print(first_non_repeating_char("leetcode"))  # Output: 'l'
print(first_non_repeating_char("aabb"))      # Output: ''
```

**Explanation:**
Count character frequencies with `Counter`. Then find the first character with frequency 1.

---

### 5. **Check Anagram**

**Problem:** Check if two strings are anagrams (same characters in different order).

**Solution:**

```python
def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

# Example
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
```

**Explanation:**
If sorting both strings produces the same sequence of characters, they are anagrams.

---

### 6. **Remove Duplicates from String**

**Problem:** Remove duplicate characters from a string while preserving order.

**Solution:**

```python
def remove_duplicates(s: str) -> str:
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

# Example
print(remove_duplicates("banana"))  # Output: "ban"
```

**Explanation:**
We track characters seen so far and only add unseen characters to the result.

---

### 7. **Check if String Contains Only Digits**

**Problem:** Check if a string consists only of digits.

**Solution:**

```python
def is_all_digits(s: str) -> bool:
    return s.isdigit()

# Example
print(is_all_digits("12345"))   # Output: True
print(is_all_digits("123a45"))  # Output: False
```

**Explanation:**
The built-in method `str.isdigit()` returns True only if all characters are digits.

---

### 8. **Count Words in a Sentence**

**Problem:** Count the number of words in a string, words are separated by spaces.

**Solution:**

```python
def count_words(s: str) -> int:
    return len(s.split())

# Example
print(count_words("Hello world! This is AI."))  # Output: 5
```

**Explanation:**
Split the string by spaces and count resulting parts.

---

### 9. **Convert to Title Case**

**Problem:** Convert a string so that the first letter of each word is capitalized.

**Solution:**

```python
def to_title_case(s: str) -> str:
    return s.title()

# Example
print(to_title_case("hello world"))  # Output: "Hello World"
```

**Explanation:**
`str.title()` capitalizes the first letter of each word.

---

### 10. **Check if String is Substring**

**Problem:** Check if one string is a substring of another.

**Solution:**

```python
def is_substring(s1: str, s2: str) -> bool:
    return s1 in s2

# Example
print(is_substring("hello", "hello world"))  # Output: True
print(is_substring("world", "hello"))        # Output: False
```

**Explanation:**
Use the `in` operator to check substring presence.

---

If you'd like, I can provide more problems or move to intermediate string problems next!
