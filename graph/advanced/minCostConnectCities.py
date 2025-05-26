"""

minimum cost to connect all cities 
Union find / Kruskal's algo

"""

def kruskal(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        
        return x
    
    def union(x,y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        
        parent[ry] = rx
        return True
    
    edges.sort(key=lambda, x: x[2])
    cost = 0
    for u, v, w in edges:
        if union(u,v):
            cost += w
    
    return cost