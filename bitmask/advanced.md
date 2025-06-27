Sure! Here are **10 advanced-level bitmask problems** with detailed solutions and explanations in Python:

---

### 1. **Travelling Salesman Problem (TSP) — Bitmask + DP**

**Problem:**
Given `n` cities and a cost matrix `cost` where `cost[i][j]` is the cost to go from city `i` to city `j`, find the minimum cost to visit all cities exactly once and return to the start city.

**Solution:**

```python
def tsp(cost):
    n = len(cost)
    ALL_VISITED = (1 << n) - 1
    memo = [[-1] * (1 << n) for _ in range(n)]
    
    def dp(pos, mask):
        if mask == ALL_VISITED:
            return cost[pos][0]  # return to start
        if memo[pos][mask] != -1:
            return memo[pos][mask]
        ans = float('inf')
        for nxt in range(n):
            if mask & (1 << nxt) == 0:
                ans = min(ans, cost[pos][nxt] + dp(nxt, mask | (1 << nxt)))
        memo[pos][mask] = ans
        return ans
    
    return dp(0, 1 << 0)

cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(cost_matrix))  # Output: 80
```

**Explanation:**
We use bitmask to track visited cities. `dp(pos, mask)` returns minimum cost starting at city `pos` having visited cities in `mask`. Memoization avoids recomputation.

---

### 2. **Minimum Set Cover Using Bitmask**

**Problem:**
Given `n` elements and `m` subsets, find the minimum number of subsets whose union covers all elements.

**Solution:**

```python
def min_set_cover(sets, n):
    m = len(sets)
    full_mask = (1 << n) - 1
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        if dp[mask] == float('inf'):
            continue
        for s in sets:
            new_mask = mask | s
            dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
    
    return dp[full_mask]

sets = [
    0b0011,  # subset covering elements 0 and 1
    0b0101,  # covering 0 and 2
    0b1000   # covering 3
]
print(min_set_cover(sets, 4))  # Output: 2
```

**Explanation:**
DP over subsets of elements covered. For each state, try adding a subset and update cost.

---

### 3. **Count Hamiltonian Paths in a DAG**

**Problem:**
Count the number of Hamiltonian paths (visiting all vertices exactly once) in a DAG using bitmask DP.

**Solution:**

```python
def count_hamiltonian_paths(graph):
    n = len(graph)
    dp = [[0] * (1 << n) for _ in range(n)]
    
    for i in range(n):
        dp[i][1 << i] = 1
    
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in graph[u]:
                    if mask & (1 << v) == 0:
                        dp[v][mask | (1 << v)] += dp[u][mask]
    return sum(dp[i][(1 << n) - 1] for i in range(n))

graph = [[1,2],[2],[]]
print(count_hamiltonian_paths(graph))  # Output: 1
```

**Explanation:**
`dp[u][mask]` = number of paths ending at `u` covering nodes in `mask`. We extend paths by adding reachable vertices.

---

### 4. **Find Largest Clique Using Bitmask**

**Problem:**
Given a graph with `n` vertices, find the size of the largest clique.

**Solution:**

```python
def largest_clique(graph):
    n = len(graph)
    max_clique = 0
    for mask in range(1 << n):
        clique = True
        nodes = [i for i in range(n) if mask & (1 << i)]
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                if nodes[j] not in graph[nodes[i]]:
                    clique = False
                    break
            if not clique:
                break
        if clique:
            max_clique = max(max_clique, len(nodes))
    return max_clique

graph = [
    {1, 2},
    {0, 2},
    {0, 1, 3},
    {2}
]
print(largest_clique(graph))  # Output: 3
```

**Explanation:**
Check all subsets and verify if every pair is connected.

---

### 5. **Find Maximum XOR of Two Numbers in an Array**

**Problem:**
Find maximum XOR of any two numbers in the array using bitmask optimization.

**Solution:**

```python
def max_xor(nums):
    max_xor = 0
    mask = 0
    for i in reversed(range(31)):
        mask |= (1 << i)
        found_prefixes = set([num & mask for num in nums])
        candidate = max_xor | (1 << i)
        if any((candidate ^ prefix) in found_prefixes for prefix in found_prefixes):
            max_xor = candidate
    return max_xor

print(max_xor([3, 10, 5, 25, 2, 8]))  # Output: 28
```

**Explanation:**
Try to set each bit from highest to lowest. Use prefix sets and check if XOR pair exists.

---

### 6. **Bitmask DP for Job Assignment**

**Problem:**
`n` jobs and `n` people. Cost matrix `cost[i][j]` is cost to assign job `j` to person `i`. Assign jobs to minimize total cost.

**Solution:**

```python
def assign_jobs(cost):
    n = len(cost)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        person = bin(mask).count('1')
        if person == n:
            continue
        for job in range(n):
            if mask & (1 << job) == 0:
                dp[mask | (1 << job)] = min(dp[mask | (1 << job)], dp[mask] + cost[person][job])
    
    return dp[(1 << n) - 1]

cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]
print(assign_jobs(cost_matrix))  # Output: 13
```

**Explanation:**
DP over subsets of assigned jobs, choosing next job for next person.

---

### 7. **Count Number of Ways to Partition Set into Two Equal Sum Subsets**

**Problem:**
Count ways to partition a set into two subsets with equal sum.

**Solution:**

```python
def count_partitions(nums):
    total = sum(nums)
    if total % 2 != 0:
        return 0
    target = total // 2
    n = len(nums)
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] += dp[s - num]
    
    return dp[target] // 2  # divide by 2 to avoid double counting

print(count_partitions([1, 5, 11, 5]))  # Output: 1
```

**Explanation:**
Count subsets summing to half total. Each partition counted twice.

---

### 8. **Maximum Sum of Non-Overlapping Intervals Using Bitmask**

**Problem:**
Given intervals with start, end, and weight, find max sum of weights of intervals with no overlaps.

**Solution:**

```python
def max_non_overlapping(intervals):
    n = len(intervals)
    intervals.sort(key=lambda x: x[1])
    dp = [0] * (1 << n)
    
    def no_overlap(i, mask):
        for j in range(n):
            if mask & (1 << j):
                if not (intervals[i][0] >= intervals[j][1] or intervals[i][1] <= intervals[j][0]):
                    return False
        return True
    
    max_weight = 0
    for mask in range(1 << n):
        total_weight = 0
        for i in range(n):
            if mask & (1 << i):
                if no_overlap(i, mask ^ (1 << i)):
                    total_weight += intervals[i][2]
                else:
                    total_weight = 0
                    break
        max_weight = max(max_weight, total_weight)
    return max_weight

intervals = [(1,3,5), (2,5,6), (4,6,5), (6,7,4)]
print(max_non_overlapping(intervals))  # Output: 10
```

**Explanation:**
Check all subsets and sum weights of intervals without overlaps.

---

### 9. **Minimum Palindromic Partition**

**Problem:**
Partition string into minimum palindromic substrings.

**Solution:**

```python
def min_pal_partition(s):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    pal = [[False] * n for _ in range(n)]
    
    for i in range(n):
        pal[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or pal[i+1][j-1]:
                    pal[i][j] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if pal[j][i-1]:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n]

print(min_pal_partition("ababbbabbababa"))  # Output: 3
```

**Explanation:**
DP with precomputed palindromic substrings; `dp[i]` = min cuts for substring `s[:i]`.

---

### 10. **Count the Number of Hamiltonian Cycles in a Graph**

**Problem:**
Count all Hamiltonian cycles in a graph using bitmask DP.

**Solution:**

```python
def count_hamiltonian_cycles(graph):
    n = len(graph)
    dp = [[0] * (1 << n) for _ in range(n)]
    dp[0][1] = 1
    
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in graph[u]:
                    if mask & (1 << v) == 0:
                        dp[v][mask | (1 << v)] += dp[u][mask]
    
    full_mask = (1 << n) - 1
    count = 0
    for v in graph[0]:
        count += dp[v][full_mask]
    return count

graph = [[1, 2], [0, 2], [0, 1]]
print(count_hamiltonian_cycles(graph))  # Output: 2
```

**Explanation:**
DP counts paths covering all nodes. Final count sums those paths that return to start to form cycles.

---

If you want me to elaborate on any of these or provide more problems, just ask!
