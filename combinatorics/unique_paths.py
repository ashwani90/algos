"""
Unique paths simple
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1 

        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]