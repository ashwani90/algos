"""

Problem: Return the number of subarrays with exactly k odd numbers.

"""


def number_of_subarrays(nums, k):
    from collections import defaultdict
    prefix = defaultdict(int)
    prefix[0] = 1
    odd_count = result = 0

    for num in nums:
        odd_count += num % 2
        result += prefix[odd_count - k]
        prefix[odd_count] += 1

    return result