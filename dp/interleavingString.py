"""

Interleaving string

check if s3 is formed by interleaving s1 and s2

"""

def isInterleave(s1,s2,s3):
    if len(s1) + len(s2) !== len(s3): return False
    dp = [[False] *(len(s2)+1) for _ in range(len(s1)+1)]
    dp[0][0] = True

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i > 0 and s1[i-1] == s3[i+j-1]:
                dp[i][j] |= dp[i-1][j]
            if j > 0 and s2[j-1] == s3[i+j-1]:
                dp[i][j] |= dp[i][j-1]
    
    return dp[-1][-1]