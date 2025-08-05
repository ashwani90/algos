"""
Problem: Return number of subarrays with sum equal to goal.
"""

from collections import defaultdict

def num_subarrays_with_sum(nums, goal):
    prefix = defaultdict(int)
    prefix[0] = 1
    total = 0
    count = 0
    for num in nums:
        total += num
        count += prefix[total-goal]
        prefix[total] += 1
    return count