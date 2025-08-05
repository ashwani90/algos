"""
Problem: Find the longest subarray where you can flip at most k 0s to 1.

"""

def longest_ones(nums, k):
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len