"""

Djikstra using min heap
find shortest path

"""

import heapq

def djikstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w 
                heapq.heappush(heap, (dist[v], v))
    
    return dist