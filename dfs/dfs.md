Absolutely! Here are **10 DFS problems** with solutions and explanations in Python:

---

### 1. **Number of Islands**

**Problem:** Given a 2D grid of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

**Solution:**

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols
            or grid[r][c] == '0' or (r, c) in visited):
            return
        visited.add((r, c))
        # Explore neighbors
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count

# Example
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(num_islands(grid))  # Output: 3
```

**Explanation:**
We run DFS from every unvisited land cell and mark all connected lands as visited, counting islands as we go.

---

### 2. **Clone Graph**

**Problem:** Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

**Solution:**

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def cloneGraph(node):
    if not node:
        return None
    visited = {}

    def dfs(n):
        if n in visited:
            return visited[n]
        copy = Node(n.val)
        visited[n] = copy
        for nei in n.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node)
```

**Explanation:**
Use DFS and a hashmap to track already cloned nodes, avoiding infinite recursion.

---

### 3. **Generate Parentheses**

**Problem:** Given `n` pairs of parentheses, generate all combinations of well-formed parentheses.

**Solution:**

```python
def generate_parenthesis(n):
    res = []

    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack()
    return res

# Example
print(generate_parenthesis(3))
# Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
```

**Explanation:**
Use DFS to build strings by adding '(' or ')' only if they keep the string valid.

---

### 4. **Word Search**

**Problem:** Given a 2D board and a word, check if the word exists in the grid following adjacent cells (up/down/left/right).

**Solution:**

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols
            or board[r][c] != word[i]):
            return False

        temp = board[r][c]
        board[r][c] = '#'  # mark visited
        found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or
                 dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        board[r][c] = temp  # restore
        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    return False

# Example
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(exist(board, "ABCCED"))  # Output: True
```

**Explanation:**
DFS explores every path matching the word, marking cells visited to avoid reuse.

---

### 5. **Number of Connected Components in an Undirected Graph**

**Problem:** Given `n` nodes and edges, count the number of connected components.

**Solution:**

```python
def count_components(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()

    def dfs(node):
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei)

    count = 0
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            count += 1
    return count

# Example
print(count_components(5, [[0,1],[1,2],[3,4]]))  # Output: 2
```

**Explanation:**
Build adjacency, DFS through each unvisited node, counting connected groups.

---

### 6. **Detect Cycle in a Directed Graph**

**Problem:** Given a directed graph, detect if there is a cycle.

**Solution:**

```python
def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for nei in graph.get(node, []):
            if nei not in visited:
                if dfs(nei):
                    return True
            elif nei in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

# Example
graph = {
    0: [1],
    1: [2],
    2: [0]
}
print(has_cycle(graph))  # Output: True
```

**Explanation:**
DFS uses recursion stack to detect back edges indicating a cycle.

---

### 7. **Find All Paths From Source to Target**

**Problem:** Given a DAG, find all paths from node 0 to node n-1.

**Solution:**

```python
def all_paths_source_target(graph):
    n = len(graph)
    res = []

    def dfs(node, path):
        if node == n - 1:
            res.append(path)
            return
        for nei in graph[node]:
            dfs(nei, path + [nei])

    dfs(0, [0])
    return res

# Example
graph = [[1,2], [3], [3], []]
print(all_paths_source_target(graph))
# Output: [[0,1,3], [0,2,3]]
```

**Explanation:**
DFS explores all paths recursively and collects completed ones.

---

### 8. **Flatten Nested List Iterator**

**Problem:** Given a nested list of integers, flatten it using DFS.

**Solution:**

```python
def flatten(nestedList):
    result = []

    def dfs(lst):
        for item in lst:
            if isinstance(item, list):
                dfs(item)
            else:
                result.append(item)

    dfs(nestedList)
    return result

# Example
nestedList = [1, [2, [3, 4], 5], 6]
print(flatten(nestedList))  # Output: [1, 2, 3, 4, 5, 6]
```

**Explanation:**
DFS recursively unpacks nested lists to collect all integers.

---

### 9. **Course Schedule (Detect if Possible to Finish All Courses)**

**Problem:** Given `numCourses` and prerequisites, check if all courses can be finished.

**Solution:**

```python
def can_finish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
        graph[pre].append(course)
    visited = set()
    rec_stack = set()

    def dfs(course):
        visited.add(course)
        rec_stack.add(course)
        for nei in graph[course]:
            if nei not in visited:
                if dfs(nei):
                    return True
            elif nei in rec_stack:
                return True
        rec_stack.remove(course)
        return False

    for course in range(numCourses):
        if course not in visited:
            if dfs(course):
                return False
    return True

# Example
print(can_finish(2, [[1,0]]))  # Output: True
print(can_finish(2, [[1,0],[0,1]]))  # Output: False
```

**Explanation:**
Detect cycles in course prerequisites with DFS.

---

### 10. **Largest Island (Modify the Number of Islands)**

**Problem:** Given a grid, you can change one `'0'` to `'1'`. Find the largest island possible.

**Solution:**

```python
def largest_island(grid):
    n = len(grid)
    index = 2
    area = {}
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def dfs(r, c, idx):
        stack = [(r, c)]
        area_count = 0
        grid[r][c] = idx
        while stack:
            x, y = stack.pop()
            area_count += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = idx
                    stack.append((nx, ny))
        return area_count

    # Label each island with an index and record area
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
               
```
Certainly! Here is the **complete solution** for the **Largest Island** problem using DFS with detailed explanation:

```python
def largest_island(grid):
    n = len(grid)
    index = 2  # start labeling islands from 2 to distinguish from 0 and 1
    area = {}  # map island index to its area (size)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def dfs(r, c, idx):
        stack = [(r, c)]
        area_count = 0
        grid[r][c] = idx
        while stack:
            x, y = stack.pop()
            area_count += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = idx
                    stack.append((nx, ny))
        return area_count

    # Label each island and calculate their area
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                area[index] = dfs(r, c, index)
                index += 1

    max_area = max(area.values()) if area else 0  # max island area without changes

    # Check each zero cell to see the combined island area if converted to 1
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                seen = set()
                combined_area = 1  # the flipped cell itself
                for dx, dy in directions:
                    nx, ny = r + dx, c + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                        idx = grid[nx][ny]
                        if idx not in seen:
                            combined_area += area[idx]
                            seen.add(idx)
                max_area = max(max_area, combined_area)

    return max_area

# Example usage:
grid = [
    [1, 0],
    [0, 1]
]
print(largest_island(grid))  # Output: 3
```

---

### Explanation:

* We first **label each island** in the grid with a unique index starting from 2 (since 0 and 1 are used).
* Using DFS, we find and label all connected cells of an island and calculate its area.
* Then, for every zero cell (water), we check its neighbors:

  * Collect the indices of distinct adjacent islands.
  * Sum their areas + 1 (for the flipped zero cell).
  * Track the maximum combined area possible.
* If the grid has no zeros, the largest island is just the biggest island area found.

This approach runs in **O(n²)** time, where `n` is grid dimension, since we label all islands once and then scan zeros once.

---

If you'd like, I can explain any part or provide more DFS problems!
