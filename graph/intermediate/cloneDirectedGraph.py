"""

Simple program to clone directed graph

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.neigbors = []

def clone_graph(node):
    if not node:
        return None
    
    visited = {}
    def dfs(n):
        if n in visited:
            return visited[n]
        
        clone = Node(n.val)
        for nei in n.neigbors:
            clone.neigbors.append(dfs(nei))
        
        return clone
    
    return dfs(node)