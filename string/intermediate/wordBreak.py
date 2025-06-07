"""

Word break

given a string and dictionary, determine if string can be segmented inti dictionary words


"""

def wordBreak(s, d):
    d = set(d)
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True

    for i in range(1, len(s)):
        for j in range(i):
            if dp[j] and s[i:j] in  d:
                    dp[i] = True
                    break
    
    return dp[n]