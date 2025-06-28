"""

Min steps to reach target in grid

"""

from collections import deque

def min_steps(grid):
    rows,cols = len(grid),len(grid[0])
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1
    
    queue = deque((0,0,0))
    visited = {(0,0)}
    while queue:
        r, c, steps = queue.popleft()
        if r == rows-1 and c == cols-1:
            return steps
        
        for dr,dc in [(1,0), (0,1), (-1,0), (0,-1)]:
            nr, nc = r + dr, c +dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, steps+1))
        
    
    return -1