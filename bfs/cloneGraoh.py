"""

Clone graph problem

Given a reference to a node in a connected undirected graph, return a deep copy of the graph.
"""


from collections import deque

class Node:
    def __init__(self, val=0, nei=None):
        self.val = val
        self.nei = nei if nei else []


def cloneGraph(node):
    if not node:
        return None
    
    visited = {}
    queue = deque([node])
    visited[node] = Node(node.val)

    while queue:
        current = queue.popleft()
        for nei in current.nei:
            if nei not in visited:
                visited[nei] = Node(nei.val)
                queue.append(nei)
            
            visited[current].nei.append(visited[nei])
    
    return visited[node]