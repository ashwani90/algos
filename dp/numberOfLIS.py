"""

Number of longest increasing subsequences

"""

def findNumberOfLis(nums):
    n = len(nums)
    dp = [1]*n
    count = [1]*n 
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    count[i] = count[j]
                elif dp[j]+1 == dp[i]:
                    count[i] += count[j]
    
    max_len = max(dp)
    return sum(c for d,c in zip(dp, count) if d == max_len)