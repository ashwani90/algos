"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxArea = 0

        def bfs(i, j):
            nonlocal maxArea
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            
            
            area += bfs(i+1, j)
            area += bfs(i, j+1)
            area += bfs(i-1, j)
            area += bfs(i, j-1)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr_area = bfs(i,j)
                    maxArea = max(maxArea, curr_area)
        
        return maxArea