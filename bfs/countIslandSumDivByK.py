class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        ct = 0
        
        def bfs(r, c):
            queue = deque([(r, c)])
            count = grid[r][c]
            grid[r][c] = 0  # mark visited
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > 0:
                        count += grid[nx][ny]
                        grid[nx][ny] = 0
                        queue.append((nx, ny))
            return count
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    count = bfs(r, c)
                    if count % k == 0:
                        ct += 1
        return ct