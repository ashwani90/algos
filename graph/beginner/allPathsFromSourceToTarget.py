"""

All paths from source to target

"""

def allPathsFromSourceToTarget(graph):

    all_paths = []

    def dfs(node, path):
        if node == end:
            all_paths.append(path)
            return
        for nei in graph[node]:
            path.append(nei)
            dfs(nei, path)
            path.pop()
    
    dfs(0, [0])
    return all_paths