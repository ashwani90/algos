"""

Topological sort Kahn's algorigthm

using indegree kahn algo

how many nodes end up at current node find that out first

"""

from collections import deque

def topo_sort(graph):
    in_degree = [0]*len(graph)

    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([i for i in range(len(graph)) if in_degree[i] == 0])

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                result.append(nei)

    return result if len(result) == len(graph) else []
# return [] if there is a cycle
