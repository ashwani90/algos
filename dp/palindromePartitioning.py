"""

Palindrome partitioning 2 (min cuts)


Return minimum number of cuts
"""

def min_cut(s):
    n = len(s)
    is_pal = [[False]*n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-2
            if s[i] == s[j] and (l==2 or is_pal[i+1][j-1]):
                is_pal[i][j] = True
    
    dp = [float("inf")] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_pal[j+1][i]:
                    d[i] = min(dp[i], dp[j]+1)
    
    return dp[-1]