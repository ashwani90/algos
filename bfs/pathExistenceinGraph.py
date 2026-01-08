'''
Problem: Given edges of an undirected graph and two nodes start and end, determine if a path exists between them.

'''

from collections import deque, defaultdict

def valid_path(n, edges, start, end):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
    
    return False