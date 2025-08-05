"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

"""

def longest_substring(s):
    chars_used = {}
    start = 0

    res = 0
    for i, char in enumerate(s):
        while char in chars_used and chars_used[char] >= start:
            start = chars_used[char] + 1
        chars_used[char] = i 
        res = max(res, i-start+1)
    return res
