Here are a few more examples of how the **Union-Find** (Disjoint Set) algorithm is applied to different problems:

---

### **Example 1: Cycle Detection in an Undirected Graph**

In an undirected graph, **cycle detection** is important for ensuring there are no cycles (e.g., in network routing, task scheduling). Union-Find is often used to detect cycles.

#### Problem:
Given an undirected graph with `n` nodes and a list of edges, check whether the graph contains a cycle.

#### Approach:
- For each edge, use the **find** operation to check if the two nodes of the edge belong to the same set.
- If they do, it means there is a cycle.
- Otherwise, union the two nodes to merge their sets.

#### Python Code:
```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Example usage: Detecting cycles
def has_cycle(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        if uf.find(u) == uf.find(v):  # Cycle detected
            return True
        uf.union(u, v)
    return False

# Graph with 5 nodes and edges
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 2)]  # This has a cycle between 2 and 4
n = 5  # Number of nodes

print(has_cycle(n, edges))  # Output: True (cycle exists)
```

---

### **Example 2: Connected Components in a Graph**

Union-Find is useful for determining how many **connected components** exist in a graph. A connected component is a set of nodes where there is a path between any two nodes.

#### Problem:
Given an undirected graph, find the number of connected components.

#### Approach:
- For each edge, unite the nodes in the edge into one component.
- At the end, count how many distinct roots (connected components) exist.

#### Python Code:
```python
def count_components(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)

    # Count the number of connected components (distinct roots)
    components = len(set(uf.find(i) for i in range(n)))
    return components

# Example usage: Counting components
edges = [(0, 1), (1, 2), (3, 4)]  # There are 2 components: {0, 1, 2} and {3, 4}
n = 5  # Number of nodes

print(count_components(n, edges))  # Output: 2
```

---

### **Example 3: Friend Circles (Social Network)**

In a social network, you can use Union-Find to track **friend circles** or groups of friends.

#### Problem:
Given a list of `n` people, where `friends[i]` is a list of friends of person `i`, find the number of friend circles.

#### Approach:
- Union every pair of friends into the same set.
- At the end, count how many distinct sets (friend circles) there are.

#### Python Code:
```python
def find_friend_circles(friends):
    n = len(friends)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if friends[i][j] == 1:  # They are friends
                uf.union(i, j)
    
    # Count the number of distinct friend circles (connected components)
    circles = len(set(uf.find(i) for i in range(n)))
    return circles

# Example usage: Counting friend circles
friends = [
    [1, 1, 0, 0],  # Person 0 is friends with 1
    [1, 1, 1, 0],  # Person 1 is friends with 0 and 2
    [0, 1, 1, 1],  # Person 2 is friends with 1 and 3
    [0, 0, 1, 1]   # Person 3 is friends with 2
]

print(find_friend_circles(friends))  # Output: 1 (Only one friend circle: {0, 1, 2, 3})
```

---

### **Example 4: Kruskal's Algorithm for Minimum Spanning Tree (MST)**

In a **weighted graph**, **Kruskal’s algorithm** uses Union-Find to efficiently find the minimum spanning tree (MST). The MST is a subset of the edges that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

#### Problem:
Find the Minimum Spanning Tree using Kruskal’s algorithm.

#### Approach:
- Sort all edges by weight.
- Add edges to the MST in order of increasing weight, but only if they do not form a cycle (checked using `find`).

#### Python Code:
```python
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight
    
    def __lt__(self, other):
        return self.weight < other.weight

def kruskal(n, edges):
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []
    
    # Sort edges by weight
    edges.sort()
    
    for edge in edges:
        u, v, weight = edge.u, edge.v, edge.weight
        if uf.find(u) != uf.find(v):  # If u and v are not in the same set
            uf.union(u, v)
            mst_weight += weight
            mst_edges.append(edge)
    
    return mst_weight, mst_edges

# Example usage: Kruskal's Algorithm
edges = [
    Edge(0, 1, 1),
    Edge(0, 2, 4),
    Edge(1, 2, 2),
    Edge(1, 3, 5),
    Edge(2, 3, 3)
]
n = 4  # Number of nodes

mst_weight, mst_edges = kruskal(n, edges)
print("MST Weight:", mst_weight)  # Output: MST Weight: 6
print("Edges in MST:", [(e.u, e.v, e.weight) for e in mst_edges])  
# Output: Edges in MST: [(0, 1, 1), (1, 2, 2), (2, 3, 3)]
```

---

### **Summary of Use Cases:**
- **Cycle Detection in Graphs**
- **Connected Components**
- **Friend Circles in Social Networks**
- **Kruskal’s Algorithm for Minimum Spanning Tree**

Each of these examples shows how Union-Find can efficiently solve problems where you need to merge sets and check if elements belong to the same set. This makes it a powerful tool for solving various graph-related problems.