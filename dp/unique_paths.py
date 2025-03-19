'''

Example 1: Unique Paths
Problem:
A robot is located at the top-left corner of an m x n grid. The robot can only move either down or right at any point in time. 
How many unique paths are there to reach the bottom-right corner?
'''

def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]