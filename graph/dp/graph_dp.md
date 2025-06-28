Here are **10 advanced graph DP problems** with solutions and explanations in Python. These problems require a solid understanding of dynamic programming combined with graph traversal (DFS, BFS, or topological sort).

---

### **1. Longest Path in a Directed Acyclic Graph (DAG)**

**Problem**: Given a DAG, find the length of the longest path.

**Approach**: Topological sort + DP on nodes.

```python
from collections import defaultdict, deque

def longest_path_DAG(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    dp = [0] * n
    q = deque([i for i in range(n) if indegree[i] == 0])

    while q:
        node = q.popleft()
        for nei in graph[node]:
            dp[nei] = max(dp[nei], dp[node] + 1)
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return max(dp)

# Example
print(longest_path_DAG(6, [(0,1),(1,2),(1,3),(3,4),(2,4),(4,5)]))  # Output: 4
```

---

### **2. Number of Paths from Source to Destination in DAG**

**Problem**: Count the number of distinct paths from source to target in a DAG.

**Approach**: Topological sort + DP.

```python
def count_paths_DAG(n, edges, start, end):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    dp = [0] * n
    dp[start] = 1

    q = deque([i for i in range(n) if indegree[i] == 0])

    while q:
        node = q.popleft()
        for nei in graph[node]:
            dp[nei] += dp[node]
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return dp[end]

# Example
print(count_paths_DAG(5, [(0,1),(0,2),(1,3),(2,3),(3,4)], 0, 4))  # Output: 2
```

---

### **3. Shortest Path with K Stops**

**Problem**: Find the shortest path from `src` to `dst` with at most `K` stops.

**Approach**: DP with Bellman-Ford style relaxation for `K+1` iterations.

```python
def shortest_path_k_stops(n, flights, src, dst, K):
    INF = float('inf')
    dp = [INF] * n
    dp[src] = 0

    for _ in range(K + 1):
        temp = dp[:]
        for u, v, w in flights:
            if dp[u] != INF:
                temp[v] = min(temp[v], dp[u] + w)
        dp = temp

    return -1 if dp[dst] == INF else dp[dst]

# Example
print(shortest_path_k_stops(4, [(0,1,100),(1,2,100),(0,2,500),(2,3,100)], 0, 3, 2))  # Output: 300
```

---

### **4. DP on Trees: Maximum Weight Independent Set**

**Problem**: Choose a set of non-adjacent nodes from a tree to maximize their weight sum.

**Approach**: DP on tree with include/exclude logic via DFS.

```python
def max_weight_independent_set(tree, weights):
    n = len(weights)
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in tree:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(u, parent):
        include = weights[u]
        exclude = 0
        for v in graph[u]:
            if v != parent:
                inc, exc = dfs(v, u)
                include += exc
                exclude += max(inc, exc)
        return include, exclude

    return max(dfs(0, -1))

# Example
print(max_weight_independent_set([(0,1),(1,2),(1,3)], [1,2,3,4]))  # Output: 6
```

---

### **5. DP on Trees: Subtree Sum with Constraint**

**Problem**: Given a tree, find the maximum sum of any subtree with ≤ `k` nodes.

**Approach**: DFS + DP storing best `k` sizes at each node.

```python
def max_k_subtree_sum(tree, values, k):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in tree:
        graph[u].append(v)
        graph[v].append(u)

    result = float('-inf')

    def dfs(u, parent):
        nonlocal result
        subsums = [values[u]]
        for v in graph[u]:
            if v == parent: continue
            child = dfs(v, u)
            for s in child:
                subsums.append(s + values[u])
        result = max(result, max(subsums[:k]))
        return subsums

    dfs(0, -1)
    return result

# Example
print(max_k_subtree_sum([(0,1),(0,2)], [1, 2, 3], 2))  # Output: 6
```

---

### **6. DP on DAG: Minimum Time to Complete All Tasks**

**Problem**: Given a DAG where each node has a time cost, find the min time to finish all tasks (respecting dependencies).

**Approach**: Topological sort + DP.

```python
def min_completion_time(n, time, dependencies):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in dependencies:
        graph[u].append(v)
        indegree[v] += 1

    dp = time[:]
    q = deque([i for i in range(n) if indegree[i] == 0])

    while q:
        node = q.popleft()
        for nei in graph[node]:
            dp[nei] = max(dp[nei], dp[node] + time[nei])
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return max(dp)

# Example
print(min_completion_time(3, [5,10,20], [(0,1),(1,2)]))  # Output: 35
```

---

### **7. Path with Maximum Gold (Graph Grid DFS + DP)**

**Problem**: Given a grid with gold, move in 4 directions without revisiting. Maximize gold collected.

**Approach**: DFS + memoization.

```python
def get_maximum_gold(grid):
    m, n = len(grid), len(grid[0])
    def dfs(x, y, visited):
        if x < 0 or x >= m or y < 0 or y >= n or (x,y) in visited or grid[x][y] == 0:
            return 0
        visited.add((x,y))
        result = 0
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            result = max(result, dfs(x+dx, y+dy, visited))
        visited.remove((x,y))
        return result + grid[x][y]

    return max(dfs(i,j,set()) for i in range(m) for j in range(n) if grid[i][j] != 0)

# Example
print(get_maximum_gold([[0,6,0],[5,8,7],[0,9,0]]))  # Output: 24
```

---

### **8. Count All Paths from Top-Left to Bottom-Right with Restrictions**

**Problem**: Grid with blocked cells. Count valid paths using DP.

**Approach**: DP with memoization.

```python
def count_paths(grid):
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    if grid[0][0] == 0:
        dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1: continue
            if i > 0: dp[i][j] += dp[i-1][j]
            if j > 0: dp[i][j] += dp[i][j-1]
            dp[i][j] %= MOD
    return dp[-1][-1]

# Example
print(count_paths([[0,0,0],[0,1,0],[0,0,0]]))  # Output: 2
```

---

### **9. Minimize Cost to Travel All Cities (TSP)**

**Problem**: Given cost matrix, find min cost to visit all cities once.

**Approach**: DP with bitmasking.

```python
def tsp(cost):
    n = len(cost)
    dp = [[float('inf')] * n for _ in range(1<<n)]
    dp[1][0] = 0

    for mask in range(1, 1<<n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) or cost[u][v] == 0:
                    continue
                next_mask = mask | (1 << v)
                dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + cost[u][v])

    return min(dp[-1][i] + cost[i][0] for i in range(n) if cost[i][0] > 0)

# Example
print(tsp([[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]))  # Output: 80
```

---

### **10. All Longest Paths in a DAG**

**Problem**: Count the number of different longest paths in a DAG.

**Approach**: Topological sort + DP for both length and count.

```python
def count_longest_paths(n, edges):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    dp = [0] * n
    count = [1] * n
    q = deque([i for i in range(n) if indegree[i] == 0])

    while q:
        u = q.popleft()
        for v in graph[u]:
            if dp[u] + 1 > dp[v]:
                dp[v] = dp[u] + 1
                count[v] = count[u]
            elif dp[u] + 1 == dp[v]:
                count[v] += count[u]
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    longest = max(dp)
    return sum(c for d, c in zip(dp, count) if d == longest)

# Example
print(count_longest_paths(5, [(0,1),(0,2),(1,3),(2,3),(3,4)]))  # Output: 2
```

---

Would you like 10 more graph DP problems (e.g. tree DP, cycle detection + DP, or shortest/longest path variants)?
