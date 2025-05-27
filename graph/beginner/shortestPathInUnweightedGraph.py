"""

Find out the shortest path in the un weighted graph

"""
from collection import deque

def shortestPath(graph):
    distance = [-1] * len(graph)
    queue = deque([start])
    distance[start] = 0

    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if distance[nei] == -1:
                distance[nei] = distance[node]+1
                queue.append(node)
    
    return distance