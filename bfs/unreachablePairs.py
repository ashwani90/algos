"""


Code
Testcase
Test Result
Test Result
2316. Count Unreachable Pairs of Nodes in an Undirected Graph
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

"""

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list first
        # Simplest way will be union find
        parent = [i for i in range(n)]
        size = [1]*n
        
        # find function
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
    
        # union the two sets
        def union(x,y):
            X = find(x)
            Y = find(y)

            if X == Y:
                return
            
            # union by size
            if size[X] < size[Y]:
                X, Y = Y, X
            parent[Y] = X
            size[X] += size[Y]
    
        for a, b in edges:
            union(a,b)
        
        component_sizes = {}
        for i in range(n):
            root = find(i)
            component_sizes[root] = component_sizes.get(root, 0) + 1
        
        total_pairs = n * (n - 1) // 2
        reachable_pairs = sum(s * (s - 1) // 2 for s in component_sizes.values())

        return total_pairs - reachable_pairs
        

            