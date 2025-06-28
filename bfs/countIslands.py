"""

Count island with 1s and water with 0s

"""

from collections import deque

def numIslands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0

    def bfs(r, c):
        queue = deque([(r,c)])
        grid[r][c] = '0'
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1,0), (0,1), (-1, 0), (0, -1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nr < rows and 0 <= nc < cols and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))

    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                bfs(r, c)
    
    return count