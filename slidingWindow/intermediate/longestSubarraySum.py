"""
Find the longest subarray with sum <= k

"""

def longest_subarray_sum_k(arr, k):
    left = 0
    total = 0
    max_len = 0
    for right in range(len(arr)):
        total += arr[right]
        while total > k:
            total -= arr[left]
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len