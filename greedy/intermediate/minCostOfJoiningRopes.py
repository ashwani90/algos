"""
Min cost of joining ropes

"""

from heapq import *

def min_cost(ropes):
    cost = 0
    heapify(ropes)
    while len(ropes) > 1:
        a = heappop(ropes)
        b = heappop(ropes)
        cost += a + b
        heappush(ropes, a+b)
    
    return cost
