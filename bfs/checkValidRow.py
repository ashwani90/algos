'''
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
'''

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        valid = set(range(1, n + 1))
        
        # Check rows
        for row in matrix:
            if set(row) != valid:
                return False
        
        # Check columns
        for col in range(n):
            col_set = set(matrix[row][col] for row in range(n))
            if col_set != valid:
                return False
        
        return True

