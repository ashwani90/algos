class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] +=1
        
        # start processing nodes that have 0 degree
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0
        order = []
        while queue:
            node = queue.popleft()
            visited += 1
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if visited == numCourses:
            return order
        return []