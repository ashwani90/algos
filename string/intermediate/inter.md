Absolutely! Here are **10 intermediate-level string problems** with **solutions and detailed explanations** in Python.

---

### 1. **Longest Substring Without Repeating Characters**

**Problem:** Given a string, find the length of the longest substring without repeating characters.

**Solution:**

```python
def length_of_longest_substring(s: str) -> int:
    start = 0
    max_length = 0
    used_chars = {}

    for i, char in enumerate(s):
        if char in used_chars and used_chars[char] >= start:
            start = used_chars[char] + 1
        used_chars[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Example
print(length_of_longest_substring("abcabcbb"))  # Output: 3 ("abc")
```

**Explanation:**
We use a sliding window approach. `start` marks the beginning of the current substring with unique chars. We move `i` forward and track last indices of chars in `used_chars`. When a repeated char is found inside the window, move `start` right after the last occurrence. Update max length as we go.

---

### 2. **Longest Palindromic Substring**

**Problem:** Find the longest palindromic substring in a given string.

**Solution:**

```python
def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    start, max_len = 0, 1

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        l1, r1 = expand_around_center(i, i)      # Odd length palindrome
        l2, r2 = expand_around_center(i, i + 1)  # Even length palindrome

        if r1 - l1 + 1 > max_len:
            start, max_len = l1, r1 - l1 + 1
        if r2 - l2 + 1 > max_len:
            start, max_len = l2, r2 - l2 + 1

    return s[start:start + max_len]

# Example
print(longest_palindrome("babad"))  # Output: "bab" or "aba"
```

**Explanation:**
We expand around each character (and between characters) to find the longest palindrome centered there. Track max palindrome boundaries and return after scanning.

---

### 3. **Group Anagrams**

**Problem:** Given a list of strings, group the anagrams together.

**Solution:**

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# Example
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

**Explanation:**
Anagrams share the same sorted character sequence. We use that as a key in a hashmap to group all anagrams together.

---

### 4. **Valid Parentheses**

**Problem:** Given a string containing only parentheses `()[]{}`, determine if it is valid (every opening bracket has a matching closing bracket in correct order).

**Solution:**

```python
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False

    return not stack

# Example
print(is_valid_parentheses("()[]{}"))  # Output: True
print(is_valid_parentheses("(]"))      # Output: False
```

**Explanation:**
We use a stack to track opening brackets. When encountering a closing bracket, pop and check if it matches the corresponding opening bracket.

---

### 5. **Minimum Window Substring**

**Problem:** Given strings `s` and `t`, find the minimum window in `s` which contains all characters of `t`.

**Solution:**

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)
    left, right = 0, 0
    formed = 0
    window_counts = {}
    min_len = float('inf')
    ans = (None, None)

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                ans = (left, right)

            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in dict_t and window_counts[left_char] < dict_t[left_char]:
                formed -= 1

            left += 1

        right += 1

    return "" if ans[0] is None else s[ans[0]:ans[1] + 1]

# Example
print(min_window("ADOBECODEBANC", "ABC"))  # Output: "BANC"
```

**Explanation:**
We use a sliding window with two pointers to cover all chars in `t`. Expand `right` to include chars, then move `left` to minimize the window while maintaining all chars.

---

### 6. **Count and Say**

**Problem:** Given an integer n, generate the nth term of the count-and-say sequence.

**Solution:**

```python
def count_and_say(n: int) -> str:
    if n == 1:
        return "1"

    prev = count_and_say(n - 1)
    result = ""
    count = 1

    for i in range(1, len(prev) + 1):
        if i < len(prev) and prev[i] == prev[i - 1]:
            count += 1
        else:
            result += str(count) + prev[i - 1]
            count = 1

    return result

# Example
print(count_and_say(4))  # Output: "1211"
```

**Explanation:**
We recursively build the sequence. For each term, read the previous term, counting consecutive digits and building the new string.

---

### 7. **Implement strStr()**

**Problem:** Find the first occurrence of a substring `needle` in string `haystack`. Return the index or -1.

**Solution:**

```python
def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

# Example
print(str_str("hello", "ll"))  # Output: 2
print(str_str("aaaaa", "bba")) # Output: -1
```

**Explanation:**
We iterate through `haystack`, checking each substring of length `needle` for equality.

---

### 8. **Count Palindromic Substrings**

**Problem:** Count how many substrings of a string are palindromes.

**Solution:**

```python
def count_palindromic_substrings(s: str) -> int:
    count = 0

    def expand_around_center(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)     # Odd length palindromes
        expand_around_center(i, i + 1) # Even length palindromes

    return count

# Example
print(count_palindromic_substrings("aaa"))  # Output: 6
```

**Explanation:**
Expand around each center (both odd and even length) counting palindromic substrings.

---

### 9. **Decode String**

**Problem:** Given an encoded string like `"3[a]2[bc]"`, decode it to `"aaabcbc"`.

**Solution:**

```python
def decode_string(s: str) -> str:
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == ']':
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char

    return current_string

# Example
print(decode_string("3[a]2[bc]"))  # Output: "aaabcbc"
```

**Explanation:**
Use a stack to handle nested encodings. Push current string and multiplier before `[`. Pop and expand after `]`.

---

### 10. **Word Break**

**Problem:** Given a string and a dictionary, determine if the string can be segmented into dictionary words.
