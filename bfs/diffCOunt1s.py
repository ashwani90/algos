"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.
"""

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        rowOnes = [0] * m
        colOnes = [0] * n
        
        # Count ones in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowOnes[i] += 1
                    colOnes[j] += 1
        
        # Build the difference matrix
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * rowOnes[i] + 2 * colOnes[j] - (m + n)
        
        return diff