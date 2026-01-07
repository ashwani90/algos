"""
There is a knight on an n x n chessboard. In a valid configuration, the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

You are given an n x n integer matrix grid consisting of distinct integers from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements or false otherwise.

Note that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell
"""


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        

        rows, cols = len(grid), len(grid[0])
        if rows == cols == 1:
            return True
        pos = {}

        for i in range(rows):
            for j in range(cols):
                pos[grid[i][j]] = (i,j)
        
        # sort the pos dict
        count = 1
        last_pos = (0,0)
        while count < rows * cols:
            dx = pos[count][0] - last_pos[0]
            dy = pos[count][1] - last_pos[1]
            if not ((abs(dx) == 2 and abs(dy) == 1) or (abs(dx) == 1 and abs(dy) == 2)):
                return False

            last_pos = pos[count]
            count += 1
        
        return True