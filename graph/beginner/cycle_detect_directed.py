"""

Detect cycle in a directed graph

"""

def detectCycleInDirectedGraph(graph):

    visited = [False]*len(graph)
    rec_stack = [False]*len(graph)

    def dfs(node):
        visited[node] = True
        rec_stack[node] = True
        for nei in graph[node]:
            if not visited[nei]:
                if dfs(nei):
                    return True
            elif rec_stack[nei]:
                return True
        rec_stack[node] = False
        return False
    
    for i in range(len(graph)):
        if not visited[i]:
            return dfs(i)
    return False