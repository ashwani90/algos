"""
Min adjacent character
"""


from heapq import *

def minAdjacent(string):
    freq = {}
    for i in string:
        freq[i] = freq.get(i, 0) + 1
    
    heap = [(-count, char) for char, count in freq.items()]
    heapify(heap)
    prev = (0, '')
    while heap:
        c, ch = heappop(heap)
        res.append(ch)
        if prev[0] < 0:
            heappush(heap, prev)
        prev = (c+1,ch )
    
    return "".join(result) if len(result) == len(string) else ""
    