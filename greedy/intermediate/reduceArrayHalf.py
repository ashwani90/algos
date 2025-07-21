"""
Reduce array size to half

"""

from collections import Counter

from heapq import *

def min_set_size(arr):
    freq = Counter(arr)
    heap = [-count for count in freq.values()]
    heapify(heap)
    removed, total, target = 0, 0, len(arr)//2
    while total < target:
        total += heappop(heap)
        removed += 1
    
    return removed