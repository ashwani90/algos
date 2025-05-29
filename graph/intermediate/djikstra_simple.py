"""

Shortest distance to all other nodes
 A heap is used

initially all distances are infinity
start distance is marked as 0 and pushed to heap as (start, 0)

loop tourhg the nei and push to queue
if distance of neig is less than what we have then correct ot
if current distance of nei is larger then node+weight then corrrect it
and push nei to heap to be checked again (like (nei, correct_dist))

"""


def djikstra(graph):
    distance = [float("inf")] * len(graph)
    distance[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        dist, node = heapq.heappop(min_heap)
        if dist > distance[node]:
            continue
        for nei, w in graph[node]:
            if distance[nei] > dist[nei] + w:
                distance[nei] = distance[nei] + w
                heapq.heappush(heap, (distance[nei], nei))

    return distance
