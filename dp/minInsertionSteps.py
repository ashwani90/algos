"""

Min insertion steps to make it a palindrome


"""

def minInsertion(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]