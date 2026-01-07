"""
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.
"""

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows,cols = len(mat), len(mat[0]) 
        freqRows = [0]*rows
        freqCols = [0]*cols
        lookup = {}

        for i in range(rows):
            for j in range(cols):
                freqRows[i] += 1
                freqCols[j] += 1
                lookup[mat[i][j]] = (i,j)
        counter = 0
        for i in arr:
            r, c = lookup[i]
            freqRows[r] -= 1
            freqCols[c] -= 1
            
            if freqRows[r] == 0 or freqCols[c] == 0:
                return counter
            counter+=1
        return -1