"""

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
"""




class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # find islands in grid2
        # increment count only if same position 1 exist in grid1
        # Let me try a little easier logical way with two pass
        rows, cols = len(grid2), len(grid2[0])
        res = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 1: Remove non-sub-island land
        for i in range(rows):
            for j in range(cols):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.bfs(grid2, i, j, rows, cols, directions)

        # Step 2: Count remaining islands in grid2
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    res += 1
                    self.bfs(grid2, i, j, rows, cols, directions)

        return res

    def bfs(self, grid, i, j, rows, cols, directions):
        queue = deque([(i, j)])
        grid[i][j] = 0  # mark visited
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))