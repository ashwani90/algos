"""

Longest palindromic strings in a given string

"""

def longestPalindromic(s):
    if not s:
        return ""
    
    start, max_len = 0, 1
    
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1
    
    for i in range(len(s)):
        l1, r1 = expandAroundCenter(i, i)
        l2, r2 = expandAroundCenter(i, i+1)

        if r1 - l1 + 1 > max_len:
            start, max_len = l1, r1-l1+1
        if r2-l2+1 > max_len:
            start, max_len = l2, r2-l2+1
    
    return s[start:start+max_len]