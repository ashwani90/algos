"""
minimum spanning tree
using kruskal algo

find total weight of a minimum spanning tree in a graph

sort edges and use UnionFind



"""

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    total = 0
    for u, v, w in edges:
        pu, pv = find(u), find(v)
        if pu != pv:
            total += w
        
    
    return total