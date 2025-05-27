"""

Simple bfs solution


"""
from collections import deque

def traverse(graph):

    que = deque(0)
    visited = [False]*len(graph)
    visited[0] = True
    while que:
        item = que.pop()
        print(item)
        for nei in graph[item]:
            if not visited[nei]:
                que.append(nei)
                visited[nei] = True
    