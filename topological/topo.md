Sure! Here are **10 topological sort problems** with detailed solutions and explanations in Python. Topological sorting applies to Directed Acyclic Graphs (DAGs) and is commonly used for scheduling, dependency resolution, and ordering tasks.

---

## 1. Basic Topological Sort (Kahn’s Algorithm)

**Problem:**
Given a DAG, return one valid topological ordering of the nodes.

**Solution:**

```python
from collections import deque, defaultdict

def topo_sort_kahn(graph, num_nodes):
    indegree = [0] * num_nodes
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    if len(topo_order) == num_nodes:
        return topo_order
    else:
        return []  # cycle detected

graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
print(topo_sort_kahn(graph, 4))  # Output: [0,1,2,3] or [0,2,1,3]
```

**Explanation:**
Kahn’s algorithm uses indegree counts and a queue. Nodes with indegree zero are added to the queue and removed step by step, producing a topological order.

---

## 2. Topological Sort Using DFS

**Problem:**
Return a topological sort of a DAG using DFS.

**Solution:**

```python
def topo_sort_dfs(graph, num_nodes):
    visited = [False] * num_nodes
    stack = []

    def dfs(u):
        visited[u] = True
        for v in graph.get(u, []):
            if not visited[v]:
                dfs(v)
        stack.append(u)

    for i in range(num_nodes):
        if not visited[i]:
            dfs(i)
    return stack[::-1]

graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
print(topo_sort_dfs(graph, 4))  # Output: [0,2,1,3] or [0,1,2,3]
```

**Explanation:**
We do DFS and push nodes to a stack after visiting all descendants. Reverse the stack to get topological order.

---

## 3. Course Schedule (LeetCode 207)

**Problem:**
There are `numCourses` courses labeled `0` to `numCourses-1`. Given prerequisites pairs `[a, b]` meaning to take course `a` you must finish course `b`, determine if you can finish all courses.

**Solution:**

```python
from collections import deque

def can_finish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0

    while queue:
        u = queue.popleft()
        count += 1
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return count == numCourses

print(can_finish(2, [[1,0]]))  # Output: True
print(can_finish(2, [[1,0],[0,1]]))  # Output: False
```

**Explanation:**
If topological order covers all courses, no cycle exists, so it is possible to finish all.

---

## 4. Find Order of Courses (LeetCode 210)

**Problem:**
Return one valid order to finish all courses given prerequisites.

**Solution:**

```python
def find_order(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return order if len(order) == numCourses else []

print(find_order(4, [[1,0],[2,0],[3,1],[3,2]]))  # Output: [0,1,2,3] or [0,2,1,3]
```

**Explanation:**
Same as Kahn’s algorithm but we return the order instead of just checking feasibility.

---

## 5. Alien Dictionary (LeetCode 269)

**Problem:**
Given a sorted dictionary of an alien language, derive the order of characters.

**Solution:**

```python
def alien_order(words):
    from collections import defaultdict, deque
    
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break
        else:
            if len(w1) > len(w2):
                return ""
    
    queue = deque([c for c in indegree if indegree[c] == 0])
    order = []
    
    while queue:
        c = queue.popleft()
        order.append(c)
        for nei in graph[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    return "".join(order) if len(order) == len(indegree) else ""

print(alien_order(["wrt","wrf","er","ett","rftt"]))  # Output: "wertf"
```

**Explanation:**
Build a graph of character precedence from adjacent words. Then use topological sort to get character order.

---

## 6. Parallel Courses III (LeetCode 2050)

**Problem:**
Given a set of courses with durations and dependencies, find the minimum time to complete all courses.

**Solution:**

```python
from collections import deque

def min_time(n, relations, time):
    graph = {i: [] for i in range(1, n+1)}
    indegree = [0] * (n+1)
    dp = [0] * (n+1)
    
    for u, v in relations:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(1, n+1) if indegree[i] == 0])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            dp[v] = max(dp[v], dp[u] + time[u-1])
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return max(dp[i] + time[i-1] for i in range(1, n+1))

print(min_time(3, [[1,3],[2,3]], [3,2,5]))  # Output: 8
```

**Explanation:**
We track earliest time each course can start using DP while doing topological sort.

---

## 7. Course Schedule IV (LeetCode 1462)

**Problem:**
Given queries asking if course `u` is a prerequisite for course `v`, answer them.

**Solution (using Floyd-Warshall or DFS+memo):**

```python
def check_if_prerequisite(n, prerequisites, queries):
    graph = [[] for _ in range(n)]
    for u, v in prerequisites:
        graph[u].append(v)
    reachable = [[False]*n for _ in range(n)]

    def dfs(u, start):
        for v in graph[u]:
            if not reachable[start][v]:
                reachable[start][v] = True
                dfs(v, start)

    for i in range(n):
        dfs(i, i)

    return [reachable[u][v] for u,v in queries]

print(check_if_prerequisite(3, [[0,1],[1,2]], [[0,2],[2,0]]))  # Output: [True, False]
```

**Explanation:**
Precompute reachability using DFS from each node, then answer queries in O(1).

---

## 8. Minimum Height Trees (LeetCode 310)

**Problem:**
Find roots of trees that produce minimum height.

**Solution (using topological sort to trim leaves):**

```python
def find_min_height_trees(n, edges):
    if n <= 2:
        return [i for i in range(n)]
    
    graph = [[] for _ in range(n)]
    indegree = [0]*n
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        indegree[u] += 1
        indegree[v] += 1

    leaves = [i for i in range(n) if indegree[i] == 1]

    remaining = n
    while remaining > 2:
        remaining -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            for nei in graph[leaf]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    new_leaves.append(nei)
        leaves = new_leaves
    return leaves

print(find_min_height_trees(4, [[1,0],[1,2],[1,3]]))  # Output: [1]
```

**Explanation:**
Trim leaf nodes iteratively, the last remaining nodes are roots of minimum height trees.

---

## 9. Find Eventual Safe States (LeetCode 802)

**Problem:**
Find all nodes in a graph that eventually lead to terminal nodes (no cycles).

**Solution:**

```python
def eventual_safe_nodes(graph):
    n = len(graph)
    color = [0]*n  # 0=unvisited, 1=visiting, 2=safe
    
    def dfs(u):
        if color[u] != 0:
            return color[u] == 2
        color[u] = 1
        for v in graph[u]:
            if color[v] == 1 or not dfs(v):
                return False
        color[u] = 2
        return True
    
    return [i for i in range(n) if dfs(i)]

print(eventual_safe_nodes([[1,2],[2,3],[5],[0],[5],[],[]]))  # Output: [2,4,5,6]
```

**Explanation:**
Use DFS + coloring to detect cycles. Nodes safe from cycles are eventual safe states.

---

## 10. Course Schedule III (LeetCode 630)

**Problem:**
Maximize number of courses taken given durations and deadlines.

\*\*Solution (uses greedy + priority queue but topological ordering is related):

```python
import heapq

def schedule_course(courses):
    courses.sort(key=lambda x: x[1])
    total_time = 0
    max_heap = []

    for duration, last_day in courses:
        total_time += duration
        heapq.heappush(max_heap, -duration)
        if total_time > last_day:
            longest = -heapq.heappop(max_heap)
            total_time -= longest
    return len(max_heap)

print(schedule_course([[100,200],[200,1300],[1000,1250],[2000,3200]]))  # Output: 3
```

**Explanation:**
Not pure topo sort but related to scheduling tasks by deadlines. Greedy approach with max heap to drop longest task when over deadline.

---

If you want me to expand on any problem or provide more variants or visualization, just ask!
