'''
There is an undirected graph with n nodes numbered from 0 to n - 1 (inclusive). You are given a 0-indexed integer array values where values[i] is the value of the ith node. You are also given a 0-indexed 2D integer array edges, where each edges[j] = [uj, vj, timej] indicates that there is an undirected edge between the nodes uj and vj, and it takes timej seconds to travel between the two nodes. Finally, you are given an integer maxTime.

A valid path in the graph is any path that starts at node 0, ends at node 0, and takes at most maxTime seconds to complete. You may visit the same node multiple times. The quality of a valid path is the sum of the values of the unique nodes visited in the path (each node's value is added at most once to the sum).

Return the maximum quality of a valid path.

Note: There are at most four edges connected to each node.

'''

class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        from collections import defaultdict

        # Build graph
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        n = len(values)
        visited = [0] * n
        self.best = 0

        def dfs(node, time_used, score):
            # If time exceeded, stop
            if time_used > maxTime:
                return

            # If we return to node 0, update answer
            if node == 0:
                self.best = max(self.best, score)

            # Explore neighbors
            for nxt, travel_time in graph[node]:
                new_time = time_used + travel_time
                if new_time > maxTime:
                    continue

                added = 0
                if visited[nxt] == 0:
                    added = values[nxt]

                visited[nxt] += 1
                dfs(nxt, new_time, score + added)
                visited[nxt] -= 1  # backtrack

        # Start DFS
        visited[0] = 1
        dfs(0, 0, values[0])

        return self.best
