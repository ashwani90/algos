"""

Minimum window substring that contains all distinct chars of a string

"""

def min_window_substring(s):
    distinct_chars = set(s)
    required = len(distinct_chars)
    window_counts = {}
    formed = 0
    l = 0
    min_len = float("inf")
    min_window = ""

    for r,char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0)
        if window_counts[char] == 1:
            formed += 1
        if formed == required:
            if r-l+1 < min_len:
                min_len = r-l+1
                min_window = s[l:r+1]
            window_counts[s[l]] -= 1
            if window_counts[s[l]] == 0:
                formed -= 1
            
            l += 1
    
    return min_window