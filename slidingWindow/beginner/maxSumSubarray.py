"""
Problem: Find the maximum sum of any contiguous subarray with size ≤ k.

"""


def max_sum_subarray_k_or_less(nums, k):
    max_sum = float('-inf')
    for size in range(1, k + 1):
        window_sum = sum(nums[:size])
        max_sum = max(max_sum, window_sum)
        for i in range(size, len(nums)):
            window_sum += nums[i] - nums[i - size]
            max_sum = max(max_sum, window_sum)
    return max_sum