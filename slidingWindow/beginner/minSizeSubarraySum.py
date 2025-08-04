"""
Problem: Given an array of positive integers and a number s, find the minimal length of a subarray for which the sum is at least s.

"""

def min_subarray_sum(s, nums):
    left = 0
    min_len = float('inf')
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]
        while curr_sum >= s:
            min_len = min(min_len, i-left+1)
            curr_sum -= nums[left]
            left += 1
    
    return 0 if min_len == float("inf") else min_len