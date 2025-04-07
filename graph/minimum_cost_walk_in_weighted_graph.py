'''
There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

 

Example 1:

Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

Output: [1,-1]

Explanation:

'''


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = y
                self.size[y] += self.size[x]
            return True
        return False

def minimum_cost(n, edges, query):
    uf = UnionFind(n)
    for u, v, w in edges:
        uf.union(u, v)

    component_cost = {}
    for u, v, w in edges:
        root = uf.find(u)
        if root not in component_cost:
            component_cost[root] = w
        else:
            component_cost[root] &= w 
    
    res = []
    for src, dst in query:
        r1, r2 = uf.find(src), uf.find(dst)
        if r1 != r2:
            res.append(-1)
        else:
            res.append(component_cost[r1])
    return res

