"""
Simple dfs graph problem
"""

def tarverse(graph):
    def dfs(node, visited):
        visited[node] = True

        for nei in graph[node]:
            if not visited[nei]:
                dfs(nei)
    
    visited = [False] * len(graph)
    dfs(0, visited)