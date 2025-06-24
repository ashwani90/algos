Sure! Here are **10 beginner-level Trie problems** with **solutions and detailed explanations** in Python. These problems cover the fundamental Trie operations and common use cases.

---

# Beginner Level Trie Problems with Solutions & Explanations

---

### 1. **Implement a Trie (Prefix Tree)**

**Problem:**
Implement a Trie with `insert`, `search`, and `startsWith` methods.

* `insert(word)`: Inserts a word into the trie.
* `search(word)`: Returns if the word is in the trie.
* `startsWith(prefix)`: Returns if any word in the trie starts with the given prefix.

**Solution:**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
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

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

**Explanation:**
A Trie is a tree where each node represents a character. We insert words by creating paths along characters, mark the end of a word, and use this structure for prefix and word search efficiently.

---

### 2. **Count Words with Given Prefix**

**Problem:**
Given a list of words, find how many words start with a given prefix.

**Solution:**

```python
class TrieNodeCount:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_end = False

class TrieCount:
    def __init__(self):
        self.root = TrieNodeCount()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNodeCount()
            node = node.children[ch]
            node.count += 1
        node.is_end = True

    def countPrefix(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count
```

**Explanation:**
We maintain a `count` at each node that keeps track of how many words pass through this node. This allows O(length of prefix) counting of words starting with that prefix.

---

### 3. **Longest Common Prefix of an Array of Strings**

**Problem:**
Find the longest common prefix string amongst an array of strings.

**Solution:**

```python
def longestCommonPrefix(strs):
    if not strs:
        return ""

    trie = Trie()
    for word in strs:
        trie.insert(word)

    prefix = ""
    node = trie.root
    while node and len(node.children) == 1 and not node.is_end_of_word:
        ch = next(iter(node.children))
        prefix += ch
        node = node.children[ch]
    return prefix
```

**Explanation:**
Insert all strings into the Trie, then walk down the Trie as long as only one child exists and it’s not the end of a word, building the longest common prefix.

---

### 4. **Check if a Word is a Concatenation of Two Words in Dictionary**

**Problem:**
Given a list of words, check if a given word can be formed by concatenating two words from the list.

**Solution:**

```python
class TrieConcat:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word, start, count=0):
        node = self.root
        for i in range(start, len(word)):
            ch = word[i]
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_end_of_word:
                if i == len(word) - 1:
                    return count >= 1
                if self.search(word, i + 1, count + 1):
                    return True
        return False

def canForm(wordList, word):
    trie = TrieConcat()
    for w in wordList:
        if w != word:
            trie.insert(w)
    return trie.search(word, 0)
```

**Explanation:**
We insert all words except the target word into a Trie. We then try to split the target word recursively and check if both parts exist in the Trie.

---

### 5. **Find All Words That Start with a Given Prefix**

**Problem:**
Given a prefix, return all words in the dictionary starting with that prefix.

**Solution:**

```python
class TrieWithWords:
    def __init__(self):
        self.root = TrieNode()
        self.words = []

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def find_words(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        result = []
        self._dfs(node, prefix, result)
        return result

    def _dfs(self, node, path, res):
        if node.is_end_of_word:
            res.append(path)
        for ch, child in node.children.items():
            self._dfs(child, path + ch, res)
```

**Explanation:**
After locating the node corresponding to the prefix, we do a DFS to collect all complete words under that node.

---

### 6. **Check If a Word Exists in Trie**

**Problem:**
Simple search to check if a word exists in the trie.

**Solution:**

```python
# This is covered in problem 1's `search` method.
```

---

### 7. **Autocomplete System**

**Problem:**
Given a dictionary and a prefix, return all autocomplete suggestions.

**Solution:**
Use problem 5's solution: find all words starting with the prefix using DFS after locating prefix node.

---

### 8. **Delete a Word from Trie**

**Problem:**
Remove a word from a trie.

**Solution:**

```python
class TrieDelete:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def delete(self, word):
        def _delete(node, word, depth):
            if not node:
                return False
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            ch = word[depth]
            if ch not in node.children:
                return False
            should_delete_child = _delete(node.children[ch], word, depth + 1)
            if should_delete_child:
                del node.children[ch]
                return not node.is_end_of_word and len(node.children) == 0
            return False
        _delete(self.root, word, 0)
```

**Explanation:**
Recursively delete nodes if they are no longer needed after removing the word.

---

### 9. **Number of Words in Trie**

**Problem:**
Count total number of words stored in the trie.

**Solution:**

```python
def count_words(node):
    count = 1 if node.is_end_of_word else 0
    for child in node.children.values():
        count += count_words(child)
    return count
```

**Explanation:**
Traverse the entire trie recursively and count nodes marked as word end.

---

### 10. **Find If There Exists Any Word That Matches a Pattern With '.' Wildcard**

**Problem:**
Search a word where '.' can match any letter.

**Solution:**

```python
class TrieWildcard:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.is_end_of_word
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)
        return dfs(self.root, 0)
```

**Explanation:**
Use DFS to explore all possible paths when encountering '.' wildcard.

---

If you want, I can provide more problems or deeper explanations on any of these. Would you like that?
