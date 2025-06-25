Sure! Here are **10 Minimum Spanning Tree (MST)** problems with solutions and explanations. Each uses classic MST algorithms like **Kruskal’s** or **Prim’s**.

---

### 1. **Find MST weight of a connected undirected graph**

**Problem:**
Given an undirected graph with weighted edges, find the weight of the MST.

**Solution:**

```python
def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0]*n
    mst_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_weight += w
    return mst_weight

# Example
n = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
print(kruskal(n, edges))  # Output: 19
```

**Explanation:**
Sort edges by weight and add them if they don’t form a cycle using union-find. The total weight is sum of MST edges.

---

### 2. **Find MST edges using Prim’s Algorithm**

**Problem:**
Find MST edges of a weighted undirected graph.

**Solution:**

```python
import heapq

def prim(n, graph):
    visited = [False]*n
    min_heap = [(0, 0)]  # (weight, vertex)
    mst_weight = 0
    mst_edges = []
    while min_heap:
        w, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_weight += w
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))
                if w != 0:
                    mst_edges.append((u, v, weight))
    return mst_weight, mst_edges

# Example graph as adjacency list
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

mst_weight, mst_edges = prim(4, graph)
print("MST weight:", mst_weight)
print("MST edges:", mst_edges)
```

**Explanation:**
Use a priority queue to greedily add the smallest edge connecting new vertices to the MST.

---

### 3. **Check if a given edge is in MST**

**Problem:**
Given a graph and an edge, check if the edge is part of any MST.

**Solution:**
An edge is in some MST iff it is a **bridge** or its weight is the smallest among all edges connecting two components.

* Use MST algorithm to check if including the edge reduces total MST weight.
* Or run MST with and without the edge and compare.

**Code sketch (conceptual):**

```python
# Build MST weight with edge included forcibly
# Build MST weight normally
# If weights are equal, edge is in some MST
```

---

### 4. **Find MST of graph with edges added dynamically**

**Problem:**
Given a graph, process queries adding edges and find MST weight after each.

**Solution:**
Use **Dynamic MST** or **Disjoint Set Union with rollback**. For beginner level:

* After each addition, rerun MST or update union-find with new edge.

---

### 5. **Count number of MSTs in a graph**

**Problem:**
Count distinct MSTs in a graph with possibly equal weight edges.

**Solution:**
Use **Kirchhoff’s theorem** (Matrix Tree Theorem) or:

* Use MST algorithm with careful counting for equal weight edges.
* More advanced, combinatorial problem.

---

### 6. **MST with maximum bottleneck edge minimized**

**Problem:**
Find MST minimizing the maximum edge weight.

**Solution:**
Regular MST already minimizes maximum edge (due to greedy property). Use Kruskal’s or Prim’s.

---

### 7. **Find MST and its total cost in a graph with negative edges**

**Problem:**
Find MST of graph with possibly negative weights.

**Solution:**
MST algorithms (Kruskal, Prim) work fine with negative weights; just sort by weight and proceed.

---

### 8. **Find MST after removing an edge**

**Problem:**
Given an MST and one edge removed, find new MST.

**Solution:**
If edge removed is not in MST, MST unchanged.

If in MST, need to add minimum weight edge connecting two disconnected components.

---

### 9. **Find MST of a complete graph with Euclidean distances**

**Problem:**
Points given, build complete graph with distances as weights and find MST.

**Solution:**

* Construct all edges from points (O(n²)).
* Run MST (Kruskal/Prim).

---

### 10. **Find MST with degree constraints**

**Problem:**
Find MST where no vertex has degree more than K.

**Solution:**
This is **Degree-constrained MST**, a hard problem, solved via heuristics or advanced algorithms.

---

If you want, I can provide full code solutions to any specific problem or explain advanced MST concepts! Would you like to start with detailed code for any of these?
