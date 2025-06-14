"""

Longest palindromic subsequence

"""

def longestPalindromic(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = i
    
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i-l+1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][-1]