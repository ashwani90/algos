Below are **10 more advanced tree-related problems**, each with a clear description, a Python solution, and an explanation of the key idea. These go beyond basic traversals into areas like data‐structures-on-trees, tree DP, and nontrivial tree constructions.

---

## 1. Segment Tree for Range Sum Query and Point Update

**Problem**
Implement a segment tree that supports:

1. Building from an initial array `arr`.
2. Querying the sum of elements in a range `[l, r]`.
3. Point‐updating `arr[i] = new_val`.

**Solution**

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        # Next power of two (for simplicity). We'll store tree in size 2*N.
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        # Initialize tree array; leaves start at index = size
        self.tree = [0] * (2 * size)
        # Build: copy leaves
        for i in range(self.n):
            self.tree[size + i] = arr[i]
        # Build internal nodes
        for i in range(size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, idx, new_val):
        # Point update: set arr[idx] = new_val
        i = self.size + idx
        self.tree[i] = new_val
        # Recompute up to root
        i //= 2
        while i > 0:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def query(self, l, r):
        # Range sum [l, r] inclusive
        res = 0
        l += self.size
        r += self.size
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res

# Example usage:
arr = [2, 1, 5, 3, 4]
st = SegmentTree(arr)
print(st.query(1, 3))  # sum arr[1..3] = 1+5+3 = 9
st.update(2, 2)        # arr[2] = 2 now
print(st.query(1, 3))  # sum arr[1..3] = 1+2+3 = 6
```

### Explanation

* We choose a “size” that’s a power of two ≥ `n`, build a full binary tree in an array of length `2*size`.
* Leaves at indices `[size…size+n−1]` hold the original values.
* Internal node `i` = sum of children at `2*i` and `2*i+1`.
* **Query**: To sum `[l, r]`, walk two pointers `l’ = l+size`, `r’ = r+size`. Whenever `l’` is a right child, include it and increment; whenever `r’` is a left child, include it and decrement; then divide both by 2.
* **Update**: Change leaf at `size+idx`, then move up updating parents.
* All operations run in O(log n).

---

## 2. Fenwick Tree (Binary Indexed Tree) for Prefix Sums

**Problem**
Implement a Fenwick Tree (BIT) to support:

1. Adding `delta` to `arr[i]`.
2. Querying the prefix sum `sum(arr[0…i])`.

**Solution**

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, delta):
        # idx: 0-based, but BIT is 1-based internally 
        i = idx + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, idx):
        # returns sum(arr[0..idx]) 
        i = idx + 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_query(self, l, r):
        return self.query(r) - (self.query(l - 1) if l > 0 else 0)

# Example usage:
arr = [3, 2, -1, 6, 5]
ft = FenwickTree(len(arr))
for i, v in enumerate(arr):
    ft.update(i, v)

print(ft.range_query(1, 3))  # sum arr[1..3] = 2 + (-1) + 6 = 7
ft.update(2, 4)              # arr[2] += 4  → now arr[2] = 3
print(ft.range_query(0, 2))  # sum arr[0..2] = 3 + 2 + 3 = 8
```

### Explanation

* Fenwick Tree stores partial sums in a 1D array where `bit[i]` aggregates a block of values.
* To **update** index `idx`, repeatedly add `delta` to `bit[i]`, then set `i += (i & -i)` (next responsible node).
* To **query** prefix sum `0…idx`, accumulate `bit[i]` then move to `i -= (i & -i)`.
* Both update and query run in O(log n).

---

## 3. Lowest Common Ancestor (LCA) with Euler Tour + RMQ

**Problem**
Preprocess a static rooted tree so that each LCA(u, v) query takes O(1) time after O(n log n) or O(n) preprocessing.

**Solution**

```python
import math

class LCA_Euler:
    def __init__(self, n, adj, root=0):
        self.n = n
        self.adj = adj
        self.euler = []
        self.depth = []
        self.first = [-1] * n
        self.visited = [False] * n
        self._dfs(root, 0)
        m = len(self.euler)
        log = math.floor(math.log2(m)) + 1
        self.st = [[0] * m for _ in range(log)]
        # Build RMQ on depth-array
        for i in range(m):
            self.st[0][i] = i
        j = 1
        while (1 << j) <= m:
            length = 1 << j
            half = length >> 1
            for i in range(m - length + 1):
                left_idx = self.st[j - 1][i]
                right_idx = self.st[j - 1][i + half]
                if self.depth[left_idx] < self.depth[right_idx]:
                    self.st[j][i] = left_idx
                else:
                    self.st[j][i] = right_idx
            j += 1

    def _dfs(self, u, d):
        self.visited[u] = True
        self.first[u] = len(self.euler)
        self.euler.append(u)
        self.depth.append(d)
        for v in self.adj[u]:
            if not self.visited[v]:
                self._dfs(v, d + 1)
                self.euler.append(u)
                self.depth.append(d)

    def _rmq(self, l, r):
        j = (r - l + 1).bit_length() - 1
        left = self.st[j][l]
        right = self.st[j][r - (1 << j) + 1]
        return left if self.depth[left] < self.depth[right] else right

    def query(self, u, v):
        l, r = self.first[u], self.first[v]
        if l > r:
            l, r = r, l
        idx = self._rmq(l, r)
        return self.euler[idx]

# Example usage:
n = 7
adj = [
    [1, 2],    # 0
    [0, 3, 4], # 1
    [0, 5, 6], # 2
    [1],       # 3
    [1],       # 4
    [2],       # 5
    [2]        # 6
]
lca = LCA_Euler(n, adj, root=0)
print(lca.query(3, 4))  # LCA(3,4)=1
print(lca.query(3, 6))  # LCA(3,6)=0
```

### Explanation

1. **Euler Tour**: Perform a DFS from `root`, append each visited node `u` to `euler` both when you enter it and each time you return from a child. Track `depth[i]` = depth of `euler[i]`. Also record `first[u]` = the first index in `euler` where `u` appears.
2. **Range Minimum Query** (RMQ): To obtain `LCA(u, v)`, look at `l = first[u]`, `r = first[v]`, take the index `k` in `[l…r]` where `depth[k]` is minimal, and return `euler[k]`.
3. Build an O(n log n) sparse table `st[j][i]` for RMQ on `depth`. Each `query(u, v)` computes `l, r`, runs RMQ in O(1).
4. Preprocessing is O(n log n); queries are O(1).

---

## 4. Count Nodes in a Complete Binary Tree in < O(n)

**Problem**
Given a complete binary tree (every level filled except possibly last, left‐filled), count its nodes in less than O(n) time.

**Solution**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def count_nodes(root):
    # If tree is empty
    if not root:
        return 0

    # Compute tree height by going as left as possible
    def left_height(node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    # Compute tree height by going as right as possible
    def right_height(node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h

    lh = left_height(root)
    rh = right_height(root)
    # If left height == right height, it's a perfect tree: 2^h - 1 nodes
    if lh == rh:
        return (1 << lh) - 1
    # Otherwise, count root (1) + recursively count left and right
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

### Explanation

* In a complete tree, if the “leftmost” path length `lh` equals the “rightmost” path `rh`, the subtree is a perfect binary tree with `(2^h − 1)` nodes.
* Otherwise, recursively count nodes in left and right subtrees.
* Each recursion reduces height by 1, so total time is O((log n)^2), not O(n).

---

## 5. Maximum Sum BST in a Binary Tree

**Problem**
In a binary tree, each node has `val`, `left`, and `right`. Find the maximum sum of all keys in any **subtree** that is a valid BST.

**Solution**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def max_sum_bst(root):
    # Return (is_bst, subtree_sum, min_val, max_val)
    # plus update a global max_sum
    max_sum = 0

    def dfs(node):
        nonlocal max_sum
        if not node:
            # An empty subtree is a BST with sum=0, min=+inf, max=−inf
            return True, 0, float('inf'), float('-inf')

        left_is_bst, left_sum, left_min, left_max = dfs(node.left)
        right_is_bst, right_sum, right_min, right_max = dfs(node.right)

        # Check BST property
        if (left_is_bst and right_is_bst and
            node.val > left_max and node.val < right_min):
            curr_sum = left_sum + node.val + right_sum
            # Update global maximum
            max_sum = max(max_sum, curr_sum)
            # New min is either left_min or node.val if left empty
            new_min = min(left_min, node.val)
            new_max = max(right_max, node.val)
            return True, curr_sum, new_min, new_max
        else:
            # Not a BST: return a marker that cannot combine upwards
            return False, 0, 0, 0

    dfs(root)
    return max_sum
```

### Explanation

* For each node, we recursively get whether left/right subtrees are BSTs, their sums, and the minimum/maximum within each subtree.
* If `node.val` > `left_max` and `< right_min`, then the subtree rooted at `node` is a BST; its sum = `left_sum + node.val + right_sum`. Update a global maximum.
* Otherwise, treat it as non-BST and propagate a flag so its ancestors won’t consider it.
* Overall, each node is visited once (O(n)).

---

## 6. Find All Nodes at Distance K in a Binary Tree

**Problem**
Given a binary tree, a target node, and an integer `K`, return all the values of nodes that are distance `K` edges from the target. (Distance counts edges, not nodes.)

**Solution**

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def distance_k(root, target, K):
    # Build adjacency-list representation to treat tree as undirected graph
    adj = {}
    def build_graph(node, parent):
        if not node: return
        if node not in adj:
            adj[node] = []
        if parent:
            adj[node].append(parent)
            adj[parent].append(node)
        build_graph(node.left, node)
        build_graph(node.right, node)

    build_graph(root, None)

    # BFS from target node out to distance K
    res = []
    visited = set([target])
    queue = deque([(target, 0)])
    while queue:
        node, dist = queue.popleft()
        if dist == K:
            res.append(node.val)
        elif dist < K:
            for nei in adj.get(node, []):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, dist + 1))
    return res
```

### Explanation

1. **Graph Building**: First DFS to build `adj[node] = [neighbors]` so that parent ↔ child edges are symmetric.
2. **BFS from Target**: Standard level-order traversal in the “undirected tree graph.” Stop when `dist == K` and collect those node values.
3. Time/O(n) to build adjacency + O(n) BFS, overall O(n).

---

## 7. Count Number of Nodes with the Same Value in Subtree (Tree DP)

**Problem**
Given a rooted tree (nodes labeled `0…n−1`) and a string `labels` where `labels[i]` is the label of node `i`. Return an array `answer` where `answer[i]` = number of nodes in the subtree of node `i` (including `i` itself) that have the same label as node `i`.

**Solution**

```python
import collections

def count_subtree_labels(n, edges, labels):
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    res = [0] * n

    def dfs(u, parent):
        # freq is a counter for all labels in this subtree
        freq = collections.Counter()
        for v in adj[u]:
            if v == parent:
                continue
            child_freq = dfs(v, u)
            # merge child_freq into freq
            for ch, count in child_freq.items():
                freq[ch] += count

        # include u itself
        freq[labels[u]] += 1
        res[u] = freq[labels[u]]
        return freq

    dfs(0, -1)  # assume 0 is root
    return res

# Example usage:
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
# Explanation: Subtree of 0 has labels {a,b,a,e,d,c,d}. `a` appears twice.
# Subtree of 1 has {b,a,e}. label[1]=='b', appears once, etc.
print(count_subtree_labels(n, edges, labels))
# Output: [2,1,1,1,1,1,1]
```

### Explanation

* We perform a DFS from the root (0). At each node `u`, gather label frequencies of its children in separate `Counter` objects, merge them, then add `labels[u]`.
* `res[u]` = `freq[labels[u]]` after merging; that is the count of `u`’s label in its entire subtree.
* Merging `Counter`s costs O(σ) where σ = size of alphabet; overall O(n · σ). If labels are lowercase English letters, σ = 26.

---

## 8. Tree DP: Maximum Independent Set in a Tree

**Problem**
Given a tree (acyclic, undirected graph) with weighted vertices, find the maximum-weight “independent set”: a set of nodes where no two are adjacent. Return the max possible sum of weights.

**Solution**

```python
import sys
sys.setrecursionlimit(10**7)

def max_independent_set(n, edges, weights):
    # Build adjacency
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # dp[u][0] = max sum in u's subtree if we do NOT pick u
    # dp[u][1] = max sum in u's subtree if we DO pick u
    dp = [[0, 0] for _ in range(n)]
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        dp[u][1] = weights[u]  # if we pick u
        dp[u][0] = 0           # if we don’t pick u
        for v in adj[u]:
            if visited[v]:
                continue
            dfs(v)
            # If we pick u, we cannot pick v
            dp[u][1] += dp[v][0]
            # If we don’t pick u, we can choose max at v
            dp[u][0] += max(dp[v][0], dp[v][1])

    dfs(0)  # assume 0 is root
    return max(dp[0][0], dp[0][1])

# Example usage:
n = 5
edges = [(0,1),(0,2),(1,3),(1,4)]
weights = [3, 2, 1, 5, 4]
# One optimal independent set: {0,3,4,2} → sum = 3 + 5 + 4 + 1 = 13
print(max_independent_set(n, edges, weights))  # 13
```

### Explanation

* We root the tree at node 0 and do a DFS.
* For each `u`, maintain two states:

  * `dp[u][1]`: maximum sum if we **pick** node `u`.
  * `dp[u][0]`: maximum sum if we **skip** node `u`.
* If we pick `u`, we must skip all children `v` (so add `dp[v][0]`).
* If we skip `u`, for each child `v` we take `max(dp[v][0], dp[v][1])` (we’re free to pick or skip the child).
* The answer is `max(dp[0][0], dp[0][1])`.
* Runs in O(n).

---

## 9. Vertical Order Traversal of a Binary Tree

**Problem**
Given a binary tree, return its **vertical order traversal**: group nodes by their column index, from leftmost column to rightmost. If two nodes share the same row and column, order by value.

**Solution**

```python
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def vertical_traversal(root):
    # Map: column → list of (row, val)
    nodes_by_col = collections.defaultdict(list)
    def dfs(node, row, col):
        if not node:
            return
        nodes_by_col[col].append((row, node.val))
        dfs(node.left, row+1, col-1)
        dfs(node.right, row+1, col+1)

    dfs(root, 0, 0)

    # Sort columns
    result = []
    for col in sorted(nodes_by_col):
        # Sort each column’s list by (row, val)
        col_list = sorted(nodes_by_col[col], key=lambda x: (x[0], x[1]))
        result.append([val for row, val in col_list])
    return result

# Example usage:
#    3
#   / \
#  9   8
# / \ / \
#4  0 1  7
#
# Vertical order: [[4],[9],[3,0,1],[8],[7]]
root = TreeNode(3,
        TreeNode(9, TreeNode(4), TreeNode(0)),
        TreeNode(8, TreeNode(1), TreeNode(7)))
print(vertical_traversal(root))
# Output: [[4],[9],[3,0,1],[8],[7]]
```

### Explanation

* Perform DFS, tracking `(row, col)` for each node. The root is `(row=0, col=0)`.
* Left child decreases `col` by 1; right child increases `col` by 1; row always increments by 1.
* Collect `(row, val)` in a dictionary keyed by `col`.
* Finally, sort columns by `col`, and within each column sort pairs by `(row ascending, value ascending)`, then output just the values.

---

## 10. Find the Centroid(s) of a Tree

**Problem**
A **centroid** of a tree is a node which, if chosen as root, minimizes the size of the largest subtree. More precisely, for a tree on n nodes, a centroid is a node such that when you remove it, every connected component has ≤ ⌊n/2⌋ nodes. Return a list of all centroids.

**Solution**

```python
def find_tree_centroids(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    size = [0] * n
    centroids = []
    def dfs(u, parent):
        size[u] = 1
        is_centroid = True
        for v in adj[u]:
            if v == parent: 
                continue
            dfs(v, u)
            size[u] += size[v]
            if size[v] > n // 2:
                is_centroid = False
        # Check “the rest of tree” excluding u’s subtree
        if n - size[u] > n // 2:
            is_centroid = False
        if is_centroid:
            centroids.append(u)

    dfs(0, -1)
    return centroids

# Example:
n = 6
edges = [(0,1),(1,2),(1,3),(3,4),(4,5)]
# The tree looks like:
#    2
#    |
#    1
#   / \
#  0   3
#       \
#        4
#         \
#          5
# Centroids are [1,3].
print(find_tree_centroids(n, edges))  # [1, 3]
```

### Explanation

* Do a DFS from any node (say 0) to compute `size[u]` = size of the subtree rooted at `u`.
* For each node `u`, check two conditions:

  1. **No child-subtree** has more than n/2 nodes.
  2. **The “complement”** (nodes outside `u`’s subtree = `n − size[u]`) is ≤ n/2.
* If both hold, `u` is a centroid. There can be one or two centroids in a tree.
* This runs in O(n).

---

### Recap of What We’ve Added

1. **Segment Tree** (Range Sum + Point Update) – O(log n) operations.
2. **Fenwick Tree** (BIT) – O(log n) prefix sums & updates.
3. **LCA via Euler Tour + RMQ** – O(1) queries after O(n log n) preprocess.
4. **Count Nodes in a Complete Tree < O(n)** – O((log n)²).
5. **Max Sum BST in a Binary Tree** – Tree DP tracking min/max of subtrees.
6. **All Nodes at Distance K** – Convert to undirected graph + BFS.
7. **Count Label-Frequency in Subtree** – DFS + Counter merging.
8. **Maximum Independent Set in a Tree** – Tree DP with “pick/skip” state.
9. **Vertical Order Traversal** – DFS tracking (row, col), sort by (col, row, val).
10. **Find Tree Centroid(s)** – DFS computing subtree sizes, check balance.

Feel free to explore these templates on your own test cases or adapt them for related tree‐DP scenarios!


Here are 20 more advanced tree problems designed to reinforce your understanding of segment trees, Fenwick trees, Euler tours, LCA, and tree DP:

---

### 🌳 Tree DP / DFS

1. **Diameter of a Tree**

   * Find the longest path between any two nodes in an unweighted tree.

2. **Maximum Path Sum in Binary Tree**

   * Find the maximum path sum between any two nodes (can go up and down).

3. **Subtree Size of Each Node**

   * Count how many nodes are in the subtree rooted at each node.

4. **Tree Coloring**

   * Minimize cost of coloring each node with given constraints on adjacent nodes.

5. **Sum of Distances in Tree**

   * For each node, compute the sum of distances to all other nodes.

6. **Minimum Vertex Cover in Tree**

   * Find minimum number of nodes such that every edge is incident to at least one of them.

7. **Longest Path with Same Value**

   * Find the length of the longest path where all nodes have the same value.

8. **Path Sum Equals K**

   * Count the number of paths in a tree whose sum equals K.

9. **House Robber III**

   * You cannot rob both a parent and its child in a tree (tree DP).

10. **Delete Tree Nodes (Pruning based on sum)**

* Delete subtrees with sum equal to 0.

---

### ⚡ Binary Lifting / LCA / Euler Tour

11. **Lowest Common Ancestor (LCA)**

* Preprocess with binary lifting, then answer queries in O(log N).

12. **K-th Ancestor of a Node**

* Find the k-th ancestor using binary lifting.

13. **LCA with Euler Tour + Segment Tree**

* Preprocess LCA using Euler tour and RMQ (Segment Tree).

14. **Distance Between Two Nodes**

* Use LCA to compute distance in log(N) time.

15. **Binary Tree Cameras**

* Place minimum cameras so every node is monitored (DP on tree).

---

### 📈 Segment Trees / Fenwick Trees on Trees

16. **Path Sum Query on Tree (Heavy-Light Decomposition or Euler Tour)**

* Handle range queries along a path in a tree.

17. **Subtree Update and Query**

* Using Euler Tour to flatten tree and apply BIT/Segment Tree.

18. **Point Update, Path Maximum Query**

* Max value between two nodes using HLD or Euler + LCA + Segment Tree.

19. **Number of Even/Odd Nodes in Subtree**

* Track count using DFS + Segment Tree/BIT.

20. **Dynamic Connectivity in Forest**

* Add/remove edges and check if nodes are connected (Link-cut trees or Euler Tour Trees).

---

If you'd like implementations for any of these, I can provide full Python code and explanations. Would you like me to start with a particular one or a group (e.g., Tree DP or LCA)?

Great! Let's continue with problems 5–10 that dive deeper into **Tree DP**, **LCA**, and **Segment Trees/Fenwick Trees on Trees**.

---

### 🌳 **5. Minimum Vertex Cover in a Tree**

**Problem**: Find the minimum number of nodes to mark so every edge has at least one endpoint marked.

**Idea**: Use DP on trees:

* `dp[u][0]`: Minimum cover if u is *not* included.
* `dp[u][1]`: Minimum cover if u *is* included.

**Code**:

```python
from collections import defaultdict

def min_vertex_cover(n, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    dp = [[0, 0] for _ in range(n)]  # dp[u][0 or 1]

    def dfs(u, parent):
        dp[u][0] = 0
        dp[u][1] = 1
        for v in tree[u]:
            if v == parent:
                continue
            dfs(v, u)
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v][0], dp[v][1])

    dfs(0, -1)
    return min(dp[0])
```

---

### 🌳 **6. Distance Between Two Nodes using LCA**

**Problem**: Given `u` and `v`, compute the distance between them.

**Idea**: Distance = `depth[u] + depth[v] - 2 * depth[lca(u, v)]`

**Code (builds on LCA code)**:

```python
def compute_distance(u, v, depth, lca):
    return depth[u] + depth[v] - 2 * depth[lca(u, v)]
```

Use the LCA setup from problem 3 to make this work.

---

### 🌳 **7. Count Nodes with Even Subtree Sum**

**Problem**: Given a value at each node, count how many subtrees have an even sum.

**Idea**: DFS to compute subtree sum, count if sum is even.

**Code**:

```python
def count_even_subtrees(tree, values):
    n = len(values)
    count = [0]

    def dfs(u, parent):
        total = values[u]
        for v in tree[u]:
            if v != parent:
                total += dfs(v, u)
        if total % 2 == 0:
            count[0] += 1
        return total

    dfs(0, -1)
    return count[0]
```

---

### 🌳 **8. Tree Path Maximum using Segment Tree + Euler Tour**

**Problem**: Update a node value and query the maximum on the path between any two nodes.

**Idea**:

* Euler Tour + Segment Tree + HLD or Binary Lifting with path jumping.

**Outline** (simplified; actual implementation is large):

* Flatten tree
* Build Segment Tree on node values
* Jump up paths using Binary Lifting until nodes match

Let me know if you want full code for this advanced version.

---

### 🌳 **9. Tree with Cameras (Binary Tree Cameras)**

**Problem**: Place the minimum number of cameras so every node is monitored.

**Idea**: Tree DP with greedy:

* 0: Node needs camera
* 1: Node has camera
* 2: Node is covered

**Code**:

```python
def min_camera_cover(root):
    res = 0

    def dfs(node):
        nonlocal res
        if not node:
            return 2
        left = dfs(node.left)
        right = dfs(node.right)
        if left == 0 or right == 0:
            res += 1
            return 1
        if left == 1 or right == 1:
            return 2
        return 0

    return res + (dfs(root) == 0)
```

---

### 🌳 **10. Count Paths with Sum = K**

**Problem**: Count number of paths (not necessarily root to leaf) in a tree that sum to K.

**Idea**: DFS + prefix sum hash map.

**Code**:

```python
def path_sum(root, target):
    from collections import defaultdict
    prefix = defaultdict(int)
    prefix[0] = 1

    def dfs(node, curr_sum):
        if not node:
            return 0
        curr_sum += node.val
        count = prefix[curr_sum - target]
        prefix[curr_sum] += 1
        count += dfs(node.left, curr_sum)
        count += dfs(node.right, curr_sum)
        prefix[curr_sum] -= 1
        return count

    return dfs(root, 0)
```

---

These 10 problems provide solid coverage of intermediate-to-advanced tree DP and traversal techniques.

Would you like me to continue with problems 11–20 (more on Euler Tour trees, HLD, dynamic trees, and segment tree applications on trees)?


Awesome! Here's the continuation with problems **11–20**, focusing on **Euler Tours, Segment/Fenwick Trees on Trees, HLD, Binary Lifting**, and **advanced dynamic tree queries**.

---

### 🌳 **11. Subtree Sum Queries with Euler Tour + Fenwick Tree**

**Problem**: For a given tree, support:

* `update(u, x)`: Add `x` to node `u`
* `query(u)`: Return the sum of all nodes in the subtree of `u`

**Idea**:

* Flatten tree using an **Euler Tour**
* Store **entry times** and use Fenwick Tree for range queries

**Code**:

```python
class FenwickTree:
    def __init__(self, n):
        self.BIT = [0] * (n + 2)

    def update(self, i, val):
        i += 1
        while i < len(self.BIT):
            self.BIT[i] += val
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i:
            res += self.BIT[i]
            i -= i & -i
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)

def subtree_sum_queries(n, tree, values):
    tin = [0]*n
    tout = [0]*n
    order = [0]*n
    time = [0]

    def dfs(u, parent):
        tin[u] = time[0]
        order[time[0]] = u
        time[0] += 1
        for v in tree[u]:
            if v != parent:
                dfs(v, u)
        tout[u] = time[0] - 1

    dfs(0, -1)

    bit = FenwickTree(n)
    for i in range(n):
        bit.update(tin[i], values[i])

    def update(u, delta):
        bit.update(tin[u], delta)

    def query(u):
        return bit.range_query(tin[u], tout[u])

    return update, query
```

---

### 🌳 **12. LCA Using Euler Tour + Segment Tree (RMQ)**

**Problem**: Use an Euler Tour and Segment Tree to find LCA.

**Idea**:

* Euler Tour records node visits + depths
* Segment Tree does RMQ on depths to find LCA

**Code** (outline):

```python
def build_euler_tour_lca(tree, n):
    euler, depth, first = [], [], [-1]*n

    def dfs(u, d, parent):
        first[u] = len(euler)
        euler.append(u)
        depth.append(d)
        for v in tree[u]:
            if v != parent:
                dfs(v, d+1, u)
                euler.append(u)
                depth.append(d)

    dfs(0, 0, -1)

    # Build segment tree for RMQ on `depth`
    from math import log2
    size = 1 << (int(log2(len(depth))) + 1)
    seg = [0] * size

    def build(i, l, r):
        if l == r:
            seg[i] = l
        else:
            m = (l + r) // 2
            build(2*i, l, m)
            build(2*i+1, m+1, r)
            seg[i] = seg[2*i] if depth[seg[2*i]] < depth[seg[2*i+1]] else seg[2*i+1]

    build(1, 0, len(depth)-1)

    def rmq(i, l, r, ql, qr):
        if r < ql or l > qr: return -1
        if ql <= l and r <= qr: return seg[i]
        m = (l + r) // 2
        left = rmq(2*i, l, m, ql, qr)
        right = rmq(2*i+1, m+1, r, ql, qr)
        if left == -1: return right
        if right == -1: return left
        return left if depth[left] < depth[right] else right

    def lca(u, v):
        l, r = first[u], first[v]
        if l > r: l, r = r, l
        return euler[rmq(1, 0, len(depth)-1, l, r)]

    return lca
```

---

### 🌳 **13. Count Even and Odd Nodes in Subtree**

**Problem**: Count even and odd valued nodes in subtree of each node.

**Idea**:

* DFS and aggregate even/odd counts from children.

**Code**:

```python
def count_even_odd_subtrees(tree, values):
    n = len(values)
    even = [0]*n
    odd = [0]*n

    def dfs(u, parent):
        even[u] = 1 if values[u] % 2 == 0 else 0
        odd[u] = 1 - even[u]
        for v in tree[u]:
            if v != parent:
                dfs(v, u)
                even[u] += even[v]
                odd[u] += odd[v]

    dfs(0, -1)
    return even, odd
```

---

### 🌳 **14. Path Minimum Query with Segment Tree and HLD**

**Problem**: Support queries of the form: minimum value along the path from `u` to `v`.

**Idea**:

* Heavy-Light Decomposition (HLD) flattens paths into contiguous ranges.
* Use segment tree over these ranges.

Let me know if you'd like the full HLD setup—it’s long but powerful.

---

### 🌳 **15. Dynamic Tree Edge Updates + Connectivity**

**Problem**: Support:

* Add/remove edge
* Check if two nodes are connected

**Idea**:

* Euler Tour Tree or Link-Cut Trees (complex)
* For limited use cases, use Union-Find with dynamic rebuilding.

Full implementation is involved—ask if you want this specifically.

---

### 🌳 **16. Ancestor with Specific Property (e.g. first with value > k)**

**Problem**: For node `u`, find the first ancestor with value > `k`.

**Idea**:

* Preprocess Binary Lifting, and for each jump track max value up the path.

---

### 🌳 **17. Tree Diameter via Double DFS**

**(Revisited for clarity)**

**Idea**:

1. DFS to find farthest node `u` from any node
2. DFS from `u` to find max distance = diameter

Fast and clean approach.

---

### 🌳 **18. Tree Height after Removing Each Node**

**Problem**: For each node, compute height of tree if that node is removed.

**Idea**:

* Use rerooting DP: simulate tree being rooted at different nodes.

---

### 🌳 **19. Rerooting DP to Compute Distances**

**Problem**: Compute `sum of distances from each node to all others`.

**Idea**:

* First DFS: compute total distance from root
* Second DFS: reroot and update answer based on parent

---

### 🌳 **20. Tree Flattening for Range Assignments**

**Problem**: Assign or increment values in subtree or path.

**Idea**:

* Euler tour + Segment Tree with lazy propagation.

---

Let me know if you'd like:

* Full code for any above
* Focused explanations (e.g., HLD, rerooting, Euler Tour techniques)
* A structured roadmap to master all tree algorithms step by step

You're making amazing progress on advanced tree topics!


Awesome! Let’s dive into detailed explanations and full Python implementations for some of those advanced tree techniques, focusing especially on **Heavy-Light Decomposition (HLD)** and **rerooting DP**, which are key for many complex tree queries.

---

# 14. Heavy-Light Decomposition (HLD) — Full Explanation and Code

### Problem Recap:

Support queries like **“What is the minimum (or max, sum, etc.) value along the path between any two nodes in a tree?”** efficiently.

---

### Why HLD?

* Tree paths aren’t contiguous in arrays, so segment trees alone don’t work on raw trees.
* HLD breaks the tree into **chains** where each chain is a heavy path.
* Paths between nodes can be decomposed into a few chains → queries become segment tree queries on chains.

---

### How HLD Works (Concept):

1. **Heavy Edge:** For each node, choose the child with the largest subtree as the heavy child; edge to it is heavy.
2. **Light Edge:** Other edges are light.
3. This splits tree into chains connected by light edges.
4. Flatten tree nodes into an array based on chains.
5. Use segment tree on this array.
6. Query path `u-v` by jumping chains up until both nodes are in the same chain.

---

### Code:

```python
import sys
sys.setrecursionlimit(10**7)

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 1
        while self.size < n: self.size <<= 1
        self.tree = [float('inf')] * (2 * self.size)

    def build(self, arr):
        for i in range(len(arr)):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])

    def update(self, pos, val):
        pos += self.size
        self.tree[pos] = val
        while pos > 1:
            pos >>= 1
            self.tree[pos] = min(self.tree[2*pos], self.tree[2*pos+1])

    def query(self, l, r):
        res = float('inf')
        l += self.size
        r += self.size
        while l <= r:
            if l & 1:
                res = min(res, self.tree[l])
                l += 1
            if not r & 1:
                res = min(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

def hld(n, edges, values):
    from collections import defaultdict
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    size = [0] * n
    depth = [0] * n
    parent = [-1] * n
    heavy = [-1] * n

    def dfs(u):
        size[u] = 1
        max_size = 0
        for v in tree[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                dfs(v)
                size[u] += size[v]
                if size[v] > max_size:
                    max_size = size[v]
                    heavy[u] = v

    dfs(0)

    head = [0] * n
    pos = [0] * n
    current_pos = [0]

    def decompose(u, h):
        head[u] = h
        pos[u] = current_pos[0]
        current_pos[0] += 1
        if heavy[u] != -1:
            decompose(heavy[u], h)
        for v in tree[u]:
            if v != parent[u] and v != heavy[u]:
                decompose(v, v)

    decompose(0, 0)

    arr = [0] * n
    for i in range(n):
        arr[pos[i]] = values[i]

    segtree = SegmentTree(n)
    segtree.build(arr)

    def query(u, v):
        res = float('inf')
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            start = head[u]
            res = min(res, segtree.query(pos[start], pos[u]))
            u = parent[start]
        if depth[u] > depth[v]:
            u, v = v, u
        res = min(res, segtree.query(pos[u], pos[v]))
        return res

    def update(u, val):
        segtree.update(pos[u], val)

    return query, update

# Example usage
n = 7
edges = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
values = [5,3,6,1,4,2,7]
query, update = hld(n, edges, values)

print(query(3,6))  # Min on path from node 3 to 6
update(3, 10)      # Update node 3's value
print(query(3,6))
```

---

# 18. Rerooting DP — Explanation and Code

### Problem Recap:

For each node, compute the **height of the tree if that node is chosen as root**.

---

### Why Rerooting?

* Naive approach: reroot the tree at each node and compute height → O(N²).
* Rerooting technique: Compute answers for root = 0, then **propagate answers** to other nodes using DP in O(N).

---

### Approach:

* First DFS: compute height from root (0).
* Second DFS: rerooting — compute answer for child based on parent’s answer.

---

### Code:

```python
from collections import defaultdict

def rerooting_height(n, edges):
    tree = defaultdict(list)
    for u,v in edges:
        tree[u].append(v)
        tree[v].append(u)

    height = [0] * n
    ans = [0] * n

    def dfs1(u, p):
        h = 0
        for v in tree[u]:
            if v == p: continue
            h = max(h, dfs1(v, u) + 1)
        height[u] = h
        return h

    def dfs2(u, p, acc):
        ans[u] = max(height[u], acc)
        prefix = [acc]
        suffix = [acc] * (len(tree[u]) + 1)

        children = [v for v in tree[u] if v != p]
        for i, v in enumerate(children):
            prefix.append(max(prefix[-1], height[v] + 1))
        for i in reversed(range(len(children))):
            suffix[i] = max(suffix[i+1], height[children[i]] + 1)

        for i, v in enumerate(children):
            use = max(prefix[i], suffix[i+1])
            dfs2(v, u, use + 1)

    dfs1(0, -1)
    dfs2(0, -1, 0)
    return ans

# Example
n = 7
edges = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
print(rerooting_height(n, edges))
```

---

If you want, I can continue with:

* More **rerooting DP** examples (like sum of distances)
* Detailed **Euler Tour + Segment Tree** for subtree queries
* More **dynamic tree data structures** like Link-Cut Trees
* Other specific problems you want!

Just say which direction you'd like to go next!
