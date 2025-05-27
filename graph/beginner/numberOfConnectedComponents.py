"""

Find out number of connected components in a graph

"""

def connectComponents(graph):
    visited = [False]*len(graph)
    count = 0

    def dfs(node):
        visited[node] = True

        for nei in graph[node]:
            if not visited[nei]:
                dfs(nei)
    for i in range(len(graph)):
        if not visited[i]:
            dfs(i)
        count += 1

    return count
