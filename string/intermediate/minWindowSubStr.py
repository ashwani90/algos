"""

Minimum window substring solution alongwith problem

"""

from collections import Counter

def minWindowSubstring(s, t):
    if not s or not t:
        return ""

    dict_t =  Counter(t)
    required = len(dict_t)
    left, right = 0, 0
    formed = 0
    window_counts = {}
    min_len = float('inf')
    ans = (None, None)

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        while left <= right and formed == required:
            if right-left+1 < min_len:
                min_len = right-left+1
                ans = (left, right)
            
            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in dict_t and window_counts[left_char]<dict_t[left_char]:
                formed -= 1
            
            left += 1
        right += 1
    
    return "" if ans[0] is None else s[ans[0]:ans[1]+1]