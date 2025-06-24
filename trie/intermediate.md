Absolutely! Here are **10 intermediate-level Trie problems** with their **solutions and detailed explanations** in Python. These problems build on the basics and introduce more complexity, like handling deletions, wildcards, complex queries, and combining tries with other techniques.

---

# Intermediate Level Trie Problems with Solutions & Explanations

---

### 1. **Implement Trie with Delete Operation**

**Problem:**
Implement a Trie with insert, search, and delete operations.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

    def delete(self, word: str) -> bool:
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            ch = word[index]
            if ch not in node.children:
                return False
            should_delete_child = _delete(node.children[ch], word, index + 1)
            if should_delete_child:
                del node.children[ch]
                return not node.is_end_of_word and len(node.children) == 0
            return False

        return _delete(self.root, word, 0)
```

**Explanation:**
The `delete` method uses recursion to remove a word, deleting nodes only if they are no longer part of another word or prefix.

---

### 2. **Word Search II — Find All Words in a Board**

**Problem:**
Given a 2D board and a list of words, find all words from the list that exist in the board. Words can be constructed from letters of sequentially adjacent cells.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def buildTrie(self, words):
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w
        return root

    def findWords(self, board, words):
        root = self.buildTrie(words)
        self.result = set()
        m, n = len(board), len(board[0])

        def dfs(i, j, node):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in node.children:
                return
            ch = board[i][j]
            next_node = node.children[ch]
            if next_node.word:
                self.result.add(next_node.word)
                next_node.word = None  # Avoid duplicates
            board[i][j] = '#'  # Mark visited
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(i + dx, j + dy, next_node)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return list(self.result)
```

**Explanation:**
Use a Trie to store words, then DFS through the board to find words that match prefixes in the Trie efficiently.

---

### 3. **Replace Words with Shortest Root in a Dictionary**

**Problem:**
Given a dictionary of roots and a sentence, replace all words in the sentence with their shortest root from the dictionary if possible.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def buildTrie(self, roots):
        root = TrieNode()
        for r in roots:
            node = root
            for ch in r:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True
        return root

    def replaceWords(self, roots, sentence):
        trie = self.buildTrie(roots)

        def replace(word):
            node = trie
            prefix = ""
            for ch in word:
                if ch not in node.children or node.is_end:
                    break
                prefix += ch
                node = node.children[ch]
            return prefix if node.is_end else word

        return ' '.join(replace(w) for w in sentence.split())
```

**Explanation:**
We build a Trie for roots. For each word, find the shortest prefix in the Trie that matches a root and replace.

---

### 4. **Count Distinct Substrings of a String**

**Problem:**
Count the number of distinct substrings of a string.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}

def countDistinctSubstrings(s):
    root = TrieNode()
    count = 0
    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            ch = s[j]
            if ch not in node.children:
                node.children[ch] = TrieNode()
                count += 1
            node = node.children[ch]
    return count + 1  # +1 for empty substring
```

**Explanation:**
Insert all suffixes of the string into a Trie; each newly created node represents a distinct substring.

---

### 5. **Longest Word in Dictionary that Can Be Built One Character at a Time**

**Problem:**
Given a list of words, find the longest word such that every prefix is also in the list.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def longestWord(self, words):
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        longest = ""

        def dfs(node, path):
            nonlocal longest
            if len(path) > len(longest) or (len(path) == len(longest) and path < longest):
                longest = path
            for ch in sorted(node.children):
                if node.children[ch].is_end:
                    dfs(node.children[ch], path + ch)

        dfs(root, "")
        return longest
```

**Explanation:**
Use DFS on the Trie, exploring only nodes where the word prefix is valid (is\_end is True). Track the longest valid word.

---

### 6. **Design a Phone Directory**

**Problem:**
Implement a system that suggests contact names from a list as the user types each character of a query string.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products, searchWord):
        root = TrieNode()
        products.sort()
        for p in products:
            node = root
            for ch in p:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(node.suggestions) < 3:
                    node.suggestions.append(p)

        res = []
        node = root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                res.append(node.suggestions)
            else:
                node = None
                res.append([])
        return res
```

**Explanation:**
At each node, keep a sorted list of up to 3 suggestions. For each character typed, return the node’s suggestion list.

---

### 7. **Find the Shortest Unique Prefix for Every Word**

**Problem:**
Given a list of words, find the shortest unique prefix for each word.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def shortestUniquePrefix(words):
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1

    result = []

    for word in words:
        node = root
        prefix = ""
        for ch in word:
            prefix += ch
            node = node.children[ch]
            if node.count == 1:
                break
        result.append(prefix)
    return result
```

**Explanation:**
We count how many words pass through each node. The first node with count 1 during traversal gives the unique prefix.

---

### 8. **Concatenated Words**

**Problem:**
Given a list of words, find all words that are concatenations of two or more words in the list.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def dfs(self, word, start, count):
        if start == len(word):
            return count >= 2
        node = self.root
        for i in range(start, len(word)):
            ch = word[i]
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_end and self.dfs(word, i+1, count+1):
                return True
        return False

    def findAllConcatenatedWords(self, words):
        for w in words:
            if w:
                self.insert(w)
        result = []
        for w in words:
            if self.dfs(w, 0, 0):
                result.append(w)
        return result
```

**Explanation:**
Use DFS with Trie to check if word can be formed by concatenation of two or more words.

---

### 9. **Longest Duplicate Substring**

**Problem:**
Find the longest substring that appears at least twice in the string.

**Solution (Using Trie for explanation, but normally suffix array/tree is better):**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = []

def longestDuplicateSubstring(s):
    root = TrieNode()
    longest = ""

    for i in range(len(s)):
        node = root
        length = 0
        for j in range(i, len(s)):
            ch = s[j]
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.indices.append(i)
            length += 1
            if len(node.indices) > 1 and length > len(longest):
                longest = s[i:i+length]
    return longest
```

**Explanation:**
For each suffix, insert into the trie and track indices. The longest substring node that has more than one index is a duplicate.

---

### 10. **Design a Data Structure for Add and Search Word with Wildcard**

**Problem:**
Add words and search with '.' wildcard character that can represent any letter.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == '.':
                return any(dfs(child, i + 1) for child in node.children.values())
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)
        return dfs(self.root, 0)
```

**Explanation:**
Use DFS with Trie nodes; '.' allows branching into all children nodes.

---

If you'd like, I can help with more advanced problems or explanations. Want me to continue?
