"""
Given a 0-indexed 2D integer matrix grid of size n * m, we define a 0-indexed 2D matrix p of size n * m as the product matrix of grid if the following condition is met:

Each element p[i][j] is calculated as the product of all elements in grid except for the element grid[i][j]. This product is then taken modulo 12345.
Return the product matrix of grid.

"""

class Solution:
    def solve(grid):
        m, n = len(grid), len(grid[0])

        prefix, suffix = [1], [1]
        
        for i in range(m):
            for j in range(n):
                prefix.append((prefix[-1] * grid[i][j]) % 12345)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                suffix.append((suffix[-1] * grid[i][j]) % 12345)
        
        for i,j in product(range(m), range(n)):
            k = i * n + j
            grid[i][j] = (prefix[k] * suffix[-k-2]) % 12345
        
        return grid
