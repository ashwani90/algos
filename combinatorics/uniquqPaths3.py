class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        total_walkable = 0
        start_row = start_col = 0

        # Lets find the starting point
        # and walkable paths
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != -1:
                    total_walkable += 1
                if grid[i][j] == 1:
                    start_row, start_col = i, j

        def dfs(r, c, remaining):
            # Valid path
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1:
                return 0
            
            # Done
            if grid[r][c] == 2:
                return 1 if remaining == 1 else 0
            
            # Mark visited
            temp = grid[r][c]
            grid[r][c] = -1 
            
            paths = (
                dfs(r + 1, c, remaining - 1) +
                dfs(r - 1, c, remaining - 1) +
                dfs(r, c + 1, remaining - 1) +
                dfs(r, c - 1, remaining - 1)
            )
            
            # Backtrack
            grid[r][c] = temp
            
            return paths

        return dfs(start_row, start_col, total_walkable)
