"""

Simple program to do topological sort of graph

"""

def topologicalSort(graph):
    visited = [False]*len(graph)
    stack = []
    def dfs(node):
        visited[node] = True
        for nei in graph[node]:
            if not visited[nei]:
                dfs(nei)
        
        stack.append(node)

    for i in range(len(graph)):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]