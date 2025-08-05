"""
Longest Repeating character replacement
Problem: Find the length of the longest substring where you can replace at most k characters to make all characters the same.
"""

def character_replacement(s, k):
    from collections import defaultdict
    left = 0
    max_len = 0
    count = defaultdict(int)
    max_count = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])
        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len