"""
Course schedule problem

Given number of courses and prerequisites, determine if all courses can be finished (no cycle).

"""

from collections import deque, defaultdict

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for neigh in graph[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)
    
    return count == numCourses