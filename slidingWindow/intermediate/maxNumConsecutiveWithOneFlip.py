"""
Problem: Given a binary array, return max consecutive 1’s if you can flip at most one 0.

"""

def max_consecutive_ones(nums):
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right-left+1)
    
    return max_len