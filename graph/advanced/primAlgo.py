"""

Prim's algo with minimum spanning tree

"""

def prim_mst(graph):
    import heapq
    n = len(graph)
    visited = [False]*n
    min_heap = [(0,0)]
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        
        visited[u] = True
        total_cost += cost
        for v,w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w,v))
    
    return total_cost