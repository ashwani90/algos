"""

Bridges in graph - Tarjan's Algo

"""

def find_bridges(graph):
    n = len(graph)
    visited = [False]*n
    disc = [0] * n
    low = [0]*n 
    time = [0]
    bridges = []

    def dfs(u, parent):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1

        for v in graph[u]:
            if v == parent:
                continue
            
            if not visited[v]:
                dfs(u, v)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            else:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    
    return bridges