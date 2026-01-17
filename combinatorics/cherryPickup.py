"""
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.

"""

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        NEG_INF = float('-inf')

        # dp[r1][c1][r2]: max cherries collected (and n*n grid)
        dp = [[[NEG_INF] * n for _ in range(n)] for _ in range(n)]

        # If can not go anywhere
        if grid[0][0] == -1:
            return 0
        dp[0][0][0] = grid[0][0] # handles initial position

        for r1 in range(n):
            for c1 in range(n):
                for r2 in range(n):
                    c2 = r1 + c1 - r2

                    # Check bounds
                    if c2 < 0 or c2 >= n:
                        continue
                    # If blocked
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue

                    # Take the best of previous states
                    best_prev = max(
                        dp[r1 - 1][c1][r2] if r1 > 0 else NEG_INF,
                        dp[r1][c1 - 1][r2] if c1 > 0 else NEG_INF,
                        dp[r1 - 1][c1][r2 - 1] if r1 > 0 and r2 > 0 else NEG_INF,
                        dp[r1][c1 - 1][r2 - 1] if c1 > 0 and r2 > 0 else NEG_INF
                    )

                    if best_prev == NEG_INF:
                        continue

                    # Collect cherries
                    cherries = grid[r1][c1]
                    if r1 != r2:
                        cherries += grid[r2][c2]

                    dp[r1][c1][r2] = best_prev + cherries

        return max(0, dp[n - 1][n - 1][n - 1])