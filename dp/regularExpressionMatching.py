"""

Regular expression matching problem
have tried with backtrack and here we will try the dp way

"""

def regularMatching(s,p):
    m, n = len(s), len(p)
    dp = [[False] * (n+1) for _ in range(m+1)]
    dp[0][0] = True

    for j in range(2,n):
        if p[j-1] == "*":
            dp[0][j] = dp[0][j-2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] in {s[j-1], '.'}:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*":
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] in {s[i-1], '.'}))
    
    return dp[m][n]
