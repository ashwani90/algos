'''

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

'''

from collections import Counter

def topKFrequentElements(nums):
    counts = Counter(nums)
    heap = []
    for i, j in counts.items():
        heapq.heappush(heap, (j,i))
        if len(heap) > k:
            heapq.heappop(heap)

    return [ num for freq, num in heap]
