Absolutely! Here are **10 advanced-level string problems** with detailed **solutions and explanations**. These problems often combine concepts like dynamic programming, advanced string algorithms, and efficient data structures.

---

### 1. **Wildcard Matching**

**Problem:** Implement wildcard pattern matching with support for `?` (matches any single character) and `*` (matches any sequence of characters, including empty).

**Solution:**

```python
def is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[m][n]

# Example
print(is_match("adceb", "*a*b"))  # Output: True
```

**Explanation:**
We use DP where `dp[i][j]` means whether `s[:i]` matches `p[:j]`. `?` matches one character, `*` matches zero or more. Two options for `*`: ignore it (`dp[i][j-1]`) or consume a char (`dp[i-1][j]`).

---

### 2. **Longest Duplicate Substring**

**Problem:** Given a string, find the longest substring that appears at least twice.

**Solution (using Binary Search + Rolling Hash):**

```python
def longest_dup_substring(S):
    mod = 2**63 - 1
    base = 256

    def check(L):
        h = 0
        seen = set()
        for i in range(L):
            h = (h * base + ord(S[i])) % mod
        seen.add(h)
        baseL = pow(base, L, mod)

        for start in range(1, len(S) - L + 1):
            h = (h * base - ord(S[start - 1]) * baseL + ord(S[start + L - 1])) % mod
            if h in seen:
                return start
            seen.add(h)
        return -1

    left, right = 1, len(S)
    start = -1
    while left <= right:
        mid = (left + right) // 2
        idx = check(mid)
        if idx != -1:
            left = mid + 1
            start = idx
        else:
            right = mid - 1

    return "" if start == -1 else S[start:start + left - 1]

# Example
print(longest_dup_substring("banana"))  # Output: "ana"
```

**Explanation:**
Binary search for the length of the duplicate substring. Use rolling hash to check if any substring of length `L` appears twice. Adjust search based on results.

---

### 3. **Regular Expression Matching**

**Problem:** Implement regex matching with `.` and `*` where `.` matches any char, `*` matches zero or more of the preceding element.

**Solution:**

```python
def is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[m][n]

# Example
print(is_match("aab", "c*a*b"))  # Output: True
```

**Explanation:**
`*` can either ignore the previous char or repeat it. DP tracks all matching states between prefixes of `s` and `p`.

---

### 4. **Minimum Window Substring with All Distinct Characters**

**Problem:** Find the minimum window substring that contains all distinct characters of a string.

**Solution:**

```python
def min_window_distinct(s: str) -> str:
    distinct_chars = set(s)
    required = len(distinct_chars)
    window_counts = {}
    formed = 0
    l = 0
    min_len = float('inf')
    min_window = ""

    for r, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        if window_counts[char] == 1:
            formed += 1

        while formed == required:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_window = s[l:r + 1]
            window_counts[s[l]] -= 1
            if window_counts[s[l]] == 0:
                formed -= 1
            l += 1

    return min_window

# Example
print(min_window_distinct("aabcbcdbca"))  # Output: "dbca"
```

**Explanation:**
Use sliding window to maintain counts of characters in current window. When all distinct chars are present, shrink window to find minimum.

---

### 5. **Edit Distance**

**Problem:** Compute the minimum number of operations (insert, delete, replace) to convert string `word1` to `word2`.

**Solution:**

```python
def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # delete
                                   dp[i][j - 1],    # insert
                                   dp[i - 1][j - 1]) # replace

    return dp[m][n]

# Example
print(min_distance("horse", "ros"))  # Output: 3
```

**Explanation:**
Use DP where each state `dp[i][j]` is min operations to convert prefixes. Recurrence considers insert, delete, replace.

---

### 6. **Suffix Array Construction**

**Problem:** Construct suffix array for a string — array of starting indices of all suffixes sorted lexicographically.

**Solution (O(n log² n)):**

```python
def build_suffix_array(s: str):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    sa = list(range(n))

    while k < n:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        tmp = [0] * n
        for i in range(1, n):
            prev, curr = sa[i - 1], sa[i]
            tmp[curr] = tmp[prev] + ((rank[prev], rank[prev + k] if prev + k < n else -1) < (rank[curr], rank[curr + k] if curr + k < n else -1))
        rank = tmp
        k <<= 1

    return sa

# Example
print(build_suffix_array("banana"))  # Output: [5, 3, 1, 0, 4, 2]
```

**Explanation:**
Rank suffixes by first k characters, then double k each iteration, sorting suffixes by two-part keys. After O(log n) iterations, suffix array is complete.

---

### 7. **Count Palindromic Substrings Using Manacher's Algorithm**

**Problem:** Count palindromic substrings in O(n) time.

**Solution:**

```python
def count_palindromes(s: str) -> int:
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    center = right = 0
    count = 0

    for i in range(n):
        mirror =
```

Sure! Continuing from **Problem 7**:

---

### 7. **Count Palindromic Substrings Using Manacher's Algorithm (continued)**

```python
def count_palindromes(s: str) -> int:
    # Transform s to add separators to handle even-length palindromes
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    center = right = 0
    count = 0

    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        # Attempt to expand palindrome centered at i
        a, b = i + p[i] + 1, i - p[i] - 1
        while a < n and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1
        # Update center and right boundary if palindrome expands past right
        if i + p[i] > right:
            center, right = i, i + p[i]
        count += (p[i] + 1) // 2  # Count palindromes contributed by center i

    return count

# Example
print(count_palindromes("aaa"))  # Output: 6
```

**Explanation:**
Manacher's algorithm transforms the string to handle odd/even palindromes uniformly by adding separators. It uses a clever symmetry property and expands palindromes centered at each position in linear time. The array `p` stores the radius of the palindrome at each center.

---

### 8. **Find All Anagrams in a String**

**Problem:** Given `s` and `p`, find all start indices of `p`'s anagrams in `s`.

**Solution:**

```python
from collections import Counter

def find_anagrams(s: str, p: str):
    p_count = Counter(p)
    s_count = Counter()
    res = []
    left = 0
    for right in range(len(s)):
        s_count[s[right]] += 1

        if right - left + 1 > len(p):
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1

        if s_count == p_count:
            res.append(left)

    return res

# Example
print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
```

**Explanation:**
Use a sliding window over `s` of size equal to `p`. Maintain a character count for the current window and compare with `p`'s count to find anagrams.

---

### 9. **Longest Common Substring**

**Problem:** Find the longest common substring between two strings.

**Solution (Using DP):**

```python
def longest_common_substring(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    end_idx = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_idx = i
            else:
                dp[i][j] = 0

    return s1[end_idx - max_len:end_idx]

# Example
print(longest_common_substring("abcdxyz", "xyzabcd"))  # Output: "abcd"
```

**Explanation:**
Use a DP table where `dp[i][j]` represents length of longest common substring ending at `s1[i-1]` and `s2[j-1]`. Keep track of max length and ending position.

---

### 10. **Word Break II**

**Problem:** Given a string `s` and a dictionary of words, return all possible sentences where `s` can be segmented into dictionary words.

**Solution:**

```python
def word_break(s: str, wordDict):
    memo = {}

    def backtrack(start):
        if start == len(s):
            return [""]

        if start in memo:
            return memo[start]

        res = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in wordDict:
                for sub in backtrack(end):
                    sentence = word + (" " + sub if sub else "")
                    res.append(sentence)
        memo[start] = res
        return res

    return backtrack(0)

# Example
print(word_break("catsanddog", {"cat", "cats", "and", "sand", "dog"}))
# Output: ["cats and dog", "cat sand dog"]
```

**Explanation:**
Use DFS + memoization to explore all segmentations starting from each index. Memo prevents recomputations for the same substring.

---

# Summary:

| #  | Problem Name                   | Key Techniques                |
| -- | ------------------------------ | ----------------------------- |
| 1  | Wildcard Matching              | DP, pattern matching          |
| 2  | Longest Duplicate Substring    | Binary search, Rolling hash   |
| 3  | Regex Matching                 | DP, pattern matching          |
| 4  | Min Window with Distinct Chars | Sliding window, hashmap       |
| 5  | Edit Distance                  | DP                            |
| 6  | Suffix Array                   | Sorting + doubling technique  |
| 7  | Manacher’s Algorithm           | Palindromic substring, linear |
| 8  | Find All Anagrams              | Sliding window, hashmap       |
| 9  | Longest Common Substring       | DP                            |
| 10 | Word Break II                  | DFS + memoization             |

If you want, I can provide code explanations, alternative approaches, or help implement any of these in other languages!
