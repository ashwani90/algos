"""
Simpel cycle deteacion in undorected graph

"""

def cycleDetect(graph):

    visited = [False]*len(graph)
    def has_cycle(node, visited, parent):

        visited[node] = True
        for nei in graph[node]:
            if not visited[nei]:
                if has_cycle(nei, visited, node):
                    return True
                elif nei != parent:
                    return True
        
        return False
    return has_cycle(0, visited, -1)