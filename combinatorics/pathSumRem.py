class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])

        # dp[row][col][remainder]
        dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]

        # Initialization
        r0 = grid[0][0] % k
        dp[0][0][r0] = 1

        for i in range(rows):
            for j in range(cols):
                for r in range(k):
                    if dp[i][j][r] == 0:
                        continue

                    # Move Down
                    if i + 1 < rows:
                        nr = (r + grid[i + 1][j]) % k
                        dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % MOD

                    # Move Right
                    if j + 1 < cols:
                        nr = (r + grid[i][j + 1]) % k
                        dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % MOD

        return dp[rows - 1][cols - 1][0]