"""
Problem: Given a 2D grid with walls (-1), gates (0), and empty rooms (INF), fill each empty room with distance to nearest gate.

"""

from collections import deque

def wallsAndGates(rooms):
    INF = 2147483647
    rows, cols = len(rooms), len(cols)

    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r,c))
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] += 1
                queue.append((nr,nc))
    
    