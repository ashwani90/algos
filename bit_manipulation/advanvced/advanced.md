Here are **10 advanced-level Bit Manipulation problems**, each with a **detailed Python solution and explanation**. These cover advanced techniques like tries, bitmask dynamic programming (DP), XOR optimization, and more.

---

### **1. Maximum XOR of Two Numbers in an Array**

**Problem**: Find the maximum XOR of any two numbers in the array.

```python
class TrieNode:
    def __init__(self):
        self.children = {}

def insert(root, num):
    node = root
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        if bit not in node.children:
            node.children[bit] = TrieNode()
        node = node.children[bit]

def find_max_xor(root, num):
    node = root
    max_xor = 0
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        toggled_bit = 1 - bit
        if toggled_bit in node.children:
            max_xor |= (1 << i)
            node = node.children[toggled_bit]
        else:
            node = node.children.get(bit, node)
    return max_xor

def findMaximumXOR(nums):
    root = TrieNode()
    for num in nums:
        insert(root, num)

    max_result = 0
    for num in nums:
        max_result = max(max_result, find_max_xor(root, num))
    return max_result

# Test
print(findMaximumXOR([3, 10, 5, 25, 2, 8]))  # 28
```

🧠 **Explanation**:
Use a binary trie to store all numbers. For each number, greedily pick opposite bits to maximize XOR.

---

### **2. Count Number of Valid Words with Bitmask Constraints**

**Problem**: Given a list of words and puzzles, count how many words can be formed from each puzzle (all puzzle letters, must include first letter).

```python
from collections import Counter

def findNumOfValidWords(words, puzzles):
    def to_mask(word):
        mask = 0
        for c in set(word):
            mask |= 1 << (ord(c) - ord('a'))
        return mask

    word_count = Counter(to_mask(word) for word in words if len(set(word)) <= 7)
    res = []

    for p in puzzles:
        total = 0
        mask = to_mask(p)
        first = 1 << (ord(p[0]) - ord('a'))

        submask = mask
        while submask:
            if submask & first:
                total += word_count.get(submask, 0)
            submask = (submask - 1) & mask
        res.append(total)
    return res

# Test
print(findNumOfValidWords(["apple","pleas","please"], ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]))  # [0, 1, 3, 2, 0]
```

🧠 **Explanation**:
Create bitmasks for words and use submask enumeration for puzzles.

---

### **3. Bitmask DP – Travelling Salesman Problem (TSP)**

**Problem**: Given a distance matrix, find the shortest path visiting all cities.

```python
def tsp(cost):
    n = len(cost)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # starting from city 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v): continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

    return min(dp[(1 << n) - 1][i] + cost[i][0] for i in range(n))

# Test
cost = [
    [0, 20, 42, 35],
    [20, 0, 30, 34],
    [42, 30, 0, 12],
    [35, 34, 12, 0]
]
print(tsp(cost))  # Shortest tour
```

🧠 **Explanation**:
Bitmask DP to represent visited cities; each state is `(mask, last_visited)`.

---

### **4. Count Bits for All Numbers up to N**

```python
def countBits(n):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i >> 1] + (i & 1)
    return res

# Test
print(countBits(5))  # [0,1,1,2,1,2]
```

🧠 **Explanation**:
`i >> 1` shifts the number; we build count based on previously computed result.

---

### **5. Smallest XOR Greater Than K**

**Problem**: Given integers `x` and `k`, find the smallest `y` such that `x ^ y > k`.

```python
def smallest_xor_greater(x, k):
    for i in range(32):
        candidate = x ^ (1 << i)
        if candidate > k:
            return candidate
    return -1

# Test
print(smallest_xor_greater(5, 6))  # 7
```

🧠 **Explanation**:
Try flipping each bit from LSB to MSB and check when `x ^ y > k`.

---

### **6. Maximum Subarray XOR**

**Problem**: Find the maximum XOR of any subarray in an array.

```python
def max_subarray_xor(nums):
    max_xor = 0
    prefix = 0
    prefixes = {0}
    for num in nums:
        prefix ^= num
        for p in prefixes:
            max_xor = max(max_xor, prefix ^ p)
        prefixes.add(prefix)
    return max_xor

# Test
print(max_subarray_xor([8, 1, 2, 12]))  # 15
```

🧠 **Explanation**:
Keep track of all prefixes; use XOR trick to find max subarray XOR.

---

### **7. Number of Set Bits in N!**

```python
def count_set_bits_in_factorial(n):
    from math import factorial
    fact = factorial(n)
    count = 0
    while fact:
        count += fact & 1
        fact >>= 1
    return count

# Test
print(count_set_bits_in_factorial(5))  # 3 (120 = 1111000)
```

🧠 **Explanation**:
Count the 1s in the binary representation of `n!`.

---

### **8. Find Unique Element Where Every Element Repeats Thrice**

```python
def single_number(nums):
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

# Test
print(single_number([2, 2, 3, 2]))  # 3
```

🧠 **Explanation**:
Track bits appearing once and twice using clever masking.

---

### **9. Check if Bits of a Number Are Alternating (101010...)**

```python
def has_alternating_bits(n):
    x = n ^ (n >> 1)
    return (x & (x + 1)) == 0

# Test
print(has_alternating_bits(5))  # True (101)
print(has_alternating_bits(7))  # False (111)
```

🧠 **Explanation**:
For alternating bits, `n ^ (n >> 1)` should be all 1s like 111...

---

### **10. Bitmask DP – Minimum Number of Semesters**

**Problem**: Minimum number of semesters to finish all courses with prerequisites.

```python
from functools import lru_cache

def minNumberOfSemesters(n, dependencies, k):
    pre = [0] * n
    for u, v in dependencies:
        pre[v - 1] |= 1 << (u - 1)

    @lru_cache(None)
    def dfs(mask):
        if mask == (1 << n) - 1:
            return 0

        can_take = []
        for i in range(n):
            if not (mask & (1 << i)) and (pre[i] & mask) == pre[i]:
                can_take.append(i)

        res = float('inf')
        for subset in subsets(can_take, k):
            new_mask = mask
            for i in subset:
                new_mask |= 1 << i
            res = min(res, 1 + dfs(new_mask))
        return res

    def subsets(arr, k):
        from itertools import combinations
        for comb in combinations(arr, min(k, len(arr))):
            yield comb

    return dfs(0)

# Test
print(minNumberOfSemesters(4, [[2,1],[3,1],[1,4]], 2))  # 3
```

🧠 **Explanation**:
Use bitmask to track completed courses and memoized DFS to minimize semesters.

---

Would you like **20 mixed bitmask DP + trie + greedy combo problems** next? Or perhaps problems that mix **bit manipulation with graph theory**?
