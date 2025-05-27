"""

Path exists between two nodes

"""

def path_exists(graph, start, end):
    visited = [False]*len(graph)
    def dfs(node):
        visited[node] = True
        if node == end:
            return True

        for nei in graph[node]:

            if not visited[nei] and dfs(nei):
                return True
        return False
    
    dfs(start)