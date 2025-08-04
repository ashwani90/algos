"""
Problem: Return the maximum for each window of size k in the array.
"""

def max_sliding_window(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        res.append(max(nums[i:i+k]))
    return res