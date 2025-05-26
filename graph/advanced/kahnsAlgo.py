"""

Kahn's algo
Topological Sorting with Cycle Detection

"""

from collections import deque

def topologicalSort(graph):
    n = len(graph)
    in_degree = [0]*n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1
        
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(order) < n:
        return None
    
    return order