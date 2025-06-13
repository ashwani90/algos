"""

count palindromic substring

"""

def countSubstring(s):
    n = len(s)
    count = 0
    dp = [[False]*n for _ in range(n)]
    for i in reversed(range(n)):
        for j in range(i, n):
            if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                dp[i][j] = True
                count += 1
    
    return count