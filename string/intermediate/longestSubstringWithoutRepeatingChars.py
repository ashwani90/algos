"""

Longest substring without repeating chars

Its a two pointer problem



"""

def longestSubstr(s):
    start = 0
    chars_used = {}
    res = 0

    for i, char in enumerate(s):
        if char in chars_used and chars_used[char] >= start:
            start = chars_used[char] + 1
        chars_used[char] = i
        res = max(res, i-start+1)
    return res