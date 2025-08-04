"""
Fruits into baskets
Problem: You are given an array where each element is a type of fruit. Pick at most two types of fruits such that the subarray is longest.

"""

def total_fruits(fruits):
    from collections import defaultdict
    left = 0
    max_len = 0
    count = defaultdict(int)

    for right in range(len(fruits)):
        count[fruits[right]] += 1
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len