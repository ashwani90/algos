"""

Problem: Given an array nums and a window size k, return the max in each sliding window.
"""

from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    res = []
    for i in range(len(nums)):
        while dq and dq[-1][0] < nums[i]:
            dq.pop()
        
        dq.append(nums[i], i)
        if dq[0][1] <= i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(dq[0][0])
    return res