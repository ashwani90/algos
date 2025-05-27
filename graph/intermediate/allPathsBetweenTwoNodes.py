"""
program to fins all paths between two nodes

"""

def find_paths(graph, start, end):
    result = []
    path = []

    def dfs(node):
        path.append(node)
        if node == end:
            result.append(path[:])
        else:
            for nei in graph[node]:
                dfs(nei)
        
        path.pop()
    
    dfs(start)
    return result