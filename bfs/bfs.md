Sure! Here are **10 BFS-based problems** along with their solutions and explanations in Python.

---

### 1. **Shortest Path in Binary Matrix**

**Problem:** Given an `n x n` binary matrix `grid`, return the length of the shortest clear path from the top-left corner to the bottom-right corner, moving in 8 directions. Return -1 if no path exists.

**Solution:**

```python
from collections import deque

def shortest_path_binary_matrix(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1
    
    directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = {(0, 0)}
    
    while queue:
        r, c, dist = queue.popleft()
        if r == n-1 and c == n-1:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1

# Explanation:
# BFS explores layer by layer and guarantees the shortest path in an unweighted grid.
```

---

### 2. **Number of Islands**

**Problem:** Given a grid of '1's (land) and '0's (water), count the number of islands.

**Solution:**

```python
from collections import deque

def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # mark visited
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                bfs(r, c)
    return count

# Explanation:
# BFS marks all connected land as visited for each island.
```

---

### 3. **Minimum Steps to Reach Target in a Grid**

**Problem:** Given a grid with obstacles, find minimum steps from start to target cell (top-left to bottom-right).

**Solution:**

```python
from collections import deque

def min_steps(grid):
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1
    
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = {(0, 0)}
    
    while queue:
        r, c, steps = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return steps
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))
    return -1

# Explanation:
# BFS finds shortest path avoiding obstacles.
```

---

### 4. **Rotting Oranges**

**Problem:** Given a grid of oranges where 2 means rotten, 1 means fresh, and 0 empty, every minute fresh oranges adjacent to rotten become rotten. Find time to rot all oranges or return -1.

**Solution:**

```python
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    
    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while queue and fresh > 0:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1
    
    return minutes if fresh == 0 else -1

# Explanation:
# BFS spreads rot in levels, counting time.
```

---

### 5. **Word Ladder**

**Problem:** Given `beginWord`, `endWord`, and a word list, find shortest transformation from begin to end, changing one letter at a time, and all intermediate words in word list.

**Solution:**

```python
from collections import deque

def word_ladder(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, length + 1))
    return 0

# Explanation:
# BFS finds shortest transformation steps.
```

---

### 6. **Clone Graph**

**Problem:** Given a reference to a node in a connected undirected graph, return a deep copy of the graph.

**Solution:**

```python
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def cloneGraph(node):
    if not node:
        return None
    
    visited = {}
    queue = deque([node])
    visited[node] = Node(node.val)
    
    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            visited[current].neighbors.append(visited[neighbor])
    
    return visited[node]

# Explanation:
# BFS visits nodes and clones neighbors.
```

---

### 7. **Course Schedule**

**Problem:** Given number of courses and prerequisites, determine if all courses can be finished (no cycle).

**Solution:**

```python
from collections import deque, defaultdict

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        for neigh in graph[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)
    
    return count == numCourses

# Explanation:
# BFS topological sort to detect cycle.
```

---

### 8. **Minimum Genetic Mutation**

**Problem:** Given start, end, and bank of gene strings, find min mutations needed to reach end from start changing one char at a time, all mutations in bank.

**Solution:**

```python
from collections import deque

def minMutation(start, end, bank):
    bank_set = set(bank)
    if end not in bank_set:
        return -1
    
    queue = deque([(start, 0)])
    visited = {start}
    genes = ['A', 'C', 'G', 'T']
    
    while queue:
        gene, steps = queue.popleft()
        if gene == end:
            return steps
        for i in range(len(gene)):
            for g in genes:
                mutation = gene[:i] + g + gene[i+1:]
                if mutation in bank_set and mutation not in visited:
                    visited.add(mutation)
                    queue.append((mutation, steps + 1))
    return -1

# Explanation:
# BFS with mutation neighbors explores shortest mutation path.
```

---

### 9. **Find the Nearest Cell with 1**

**Problem:** Given a grid of 0s and 1s, for each cell find the distance to the nearest cell containing 1.

**Solution:**

```python
from collections import deque

def nearest_one(grid):
    rows, cols = len(grid), len(grid[0])
    dist = [[-1]*cols for _ in range(rows)]
    queue = deque()
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist

# Explanation:
# Multi-source BFS starting from all 1's simultaneously.
```

---

### 10. **Walls and Gates**

**Problem:** Given a 2D grid with walls (-1), gates (0), and empty rooms (INF), fill each empty room with distance to nearest gate.

**Solution:**

```python
from collections import deque

def walls_and_gates(rooms):
    INF = 2147483647
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()
    
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))

# Explanation:
# BFS starting from all gates simultaneously to fill nearest distances.
```

---

If you want detailed explanations for any problem or more BFS problems, feel free to ask!

Sure! Here are **more BFS problems** with solutions and explanations:

---

### 11. **Find if Path Exists in Graph**

**Problem:** Given edges of an undirected graph and two nodes `start` and `end`, determine if a path exists between them.

**Solution:**

```python
from collections import deque, defaultdict

def valid_path(n, edges, start, end):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

# Explanation:
# BFS explores all reachable nodes from start. If end is reached, path exists.
```

---

### 12. **Minimum Knight Moves**

**Problem:** Given a chessboard, find the minimum number of knight moves to reach from (0,0) to (x,y).

**Solution:**

```python
from collections import deque

def min_knight_moves(x, y):
    directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    visited = set([(0,0)])
    queue = deque([(0,0,0)])  # x, y, steps
    
    while queue:
        cx, cy, steps = queue.popleft()
        if (cx, cy) == (x, y):
            return steps
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # Limit search space based on symmetry and reasonableness
            if (nx, ny) not in visited and nx >= -2 and ny >= -2:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

# Explanation:
# BFS finds shortest moves on unweighted chessboard.
```

---

### 13. **Sliding Puzzle**

**Problem:** Given a 2x3 board, move tiles to reach target state. Return minimum moves or -1 if unsolvable.

**Solution:**

```python
from collections import deque

def sliding_puzzle(board):
    start = ''.join(str(num) for row in board for num in row)
    target = '123450'
    neighbors = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }

    queue = deque([(start, start.index('0'), 0)])
    visited = {start}

    while queue:
        state, zero, moves = queue.popleft()
        if state == target:
            return moves
        
        for neighbor in neighbors[zero]:
            new_state = list(state)
            new_state[zero], new_state[neighbor] = new_state[neighbor], new_state[zero]
            new_state_str = ''.join(new_state)
            if new_state_str not in visited:
                visited.add(new_state_str)
                queue.append((new_state_str, neighbor, moves + 1))
    return -1

# Explanation:
# BFS over states finds minimal moves to solve sliding puzzle.
```

---

### 14. **Shortest Distance from All Buildings**

**Problem:** Given a grid with buildings (1), empty land (0), and obstacles (2), find the shortest distance from an empty land to all buildings.

**Solution:**

```python
from collections import deque

def shortest_distance(grid):
    rows, cols = len(grid), len(grid[0])
    total_buildings = sum(val == 1 for row in grid for val in row)
    distance = [[0]*cols for _ in range(rows)]
    reach = [[0]*cols for _ in range(rows)]

    def bfs(start_r, start_c):
        visited = [[False]*cols for _ in range(rows)]
        queue = deque([(start_r, start_c, 0)])
        visited[start_r][start_c] = True
        
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        distance[nr][nc] += dist + 1
                        reach[nr][nc] += 1
                        queue.append((nr, nc, dist + 1))
                    elif grid[nr][nc] == 1:
                        visited[nr][nc] = True

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                bfs(r, c)

    shortest = float('inf')
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and reach[r][c] == total_buildings:
                shortest = min(shortest, distance[r][c])
    return shortest if shortest != float('inf') else -1

# Explanation:
# BFS from each building accumulates distances; find minimal reachable empty cell.
```

---

### 15. **Alien Dictionary**

**Problem:** Given a sorted dictionary of an alien language, derive the order of characters.

**Solution:**

```python
from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}
    
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break
        else:
            if len(w2) < len(w1):
                return ""
    
    queue = deque([c for c in indegree if indegree[c] == 0])
    order = []
    while queue:
        c = queue.popleft()
        order.append(c)
        for neigh in graph[c]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)
    if len(order) < len(indegree):
        return ""
    return "".join(order)

# Explanation:
# Topological sort of characters from adjacent word comparisons.
```

---

### 16. **Find the Shortest Bridge**

**Problem:** Given a grid with two islands, find shortest bridge (flip 0s to 1s) to connect islands.

**Solution:**

```python
from collections import deque

def shortest_bridge(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c, q):
        if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == 0:
            return
        visited.add((r,c))
        q.append((r,c))
        dfs(r+1,c,q)
        dfs(r-1,c,q)
        dfs(r,c+1,q)
        dfs(r,c-1,q)

    queue = deque()
    found = False
    for r in range(rows):
        if found:
            break
        for c in range(cols):
            if grid[r][c] == 1:
                dfs(r, c, queue)
                found = True
                break

    steps = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    if grid[nr][nc] == 1:
                        return steps
                    visited.add((nr,nc))
                    queue.append((nr,nc))
        steps += 1

# Explanation:
# BFS expands from one island to find shortest connection to other.
```

---

### 17. **Pacific Atlantic Water Flow**

**Problem:** Given a matrix, find cells from which water can flow to both Pacific and Atlantic oceans.

**Solution:**

```python
from collections import deque

def pacific_atlantic(matrix):
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    pacific = set()
    atlantic = set()
    
    def bfs(starts, visited):
        queue = deque(starts)
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and matrix[nr][nc] >= matrix[r][c]:
                    visited.add((nr,nc))
                    queue.append((nr,nc))
    
    pac
```
