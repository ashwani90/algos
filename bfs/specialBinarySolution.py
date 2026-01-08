"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
"""

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        grid = mat
        m, n = len(grid), len(grid[0])
        
        rowOnes = [0] * m
        colOnes = [0] * n
        
        # Count ones in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowOnes[i] += 1
                    colOnes[j] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and rowOnes[i] == 1 and colOnes[j] == 1:
                    res += 1
        
        return res

