"""
IPO Problem
# Given projects with profits and capital, select at most k projects to maximize capital starting with w.


"""

import heapq
def find_max_capital(k, w, profits, capital):
    projects = sorted(zip(capital, profits))

    heap = []
    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(heap, -projects[i][1])
            i+=1
        
        if not heap:
            break
        w -= heapq.heappop(heap)
    
    return w