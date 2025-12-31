"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
"""

from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0
        
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                sub = [row[j:j+3] for row in grid[i:i+3]]
                if self.check_magicSquare(sub):
                    count += 1
        return count

    def check_magicSquare(self, grid):
        # Must contain digits 1–9 exactly once
        nums = set()
        for row in grid:
            for val in row:
                if val < 1 or val > 9:
                    return False
                nums.add(val)
        if len(nums) != 9:
            return False

        target = sum(grid[0])

        # Check rows
        for row in grid:
            if sum(row) != target:
                return False

        # Check columns
        for c in range(3):
            if grid[0][c] + grid[1][c] + grid[2][c] != target:
                return False

        # Check diagonals
        if grid[0][0] + grid[1][1] + grid[2][2] != target:
            return False
        if grid[0][2] + grid[1][1] + grid[2][0] != target:
            return False

        return True
