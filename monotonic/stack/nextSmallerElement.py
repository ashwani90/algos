"""
Get next smaller element problem
"""

def next_smaller(nums):
    res = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[stack[-1]] > nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    
    return res