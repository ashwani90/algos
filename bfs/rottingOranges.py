"""

Rotting oranges py function

"""

def rottingOranges(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r,c))
            elif grid[r][c] == 1:
                fresh += 1
    
    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue and fresh > 0:
        