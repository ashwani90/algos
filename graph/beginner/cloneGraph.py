"""

Simple program to clone a graph

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.neigbours = []

def clone_graph(node):
    if not node:
        return None

    old_to_new = {}
    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]
        
        copy = Node(node.val)
        for nei in graph[node]:
            copy.neigbours.append(dfs(nei))
        
        return copy
    
    return dfs(node)