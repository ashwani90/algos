"""
If we start to color graphs then two colors should be suffice tp color it
and no connected nodes will have same color



"""

from collections import deque

def bipartiateGraph(graph):
    color = [-1] * len(graph)

    for i in range(len(graph)):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1-color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False

    return True