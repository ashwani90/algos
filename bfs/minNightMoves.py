"""
Given a chessboard, find the minimum number of knight moves to reach from (0,0) to (x,y).

"""

from collections import deque

def min_night_moves(x, y):
    directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

    visited = set([(0,0)])
    queue = deque([(0,0,0)]) # x, y, steps

    while queue:
        cx, cy, step = queue.popleft()
        if (cx, cy) == (x,y):
            return steps
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if (nx, ny) not in visited and nx >= -2 and ny >= -2:
                visited.add((nx,ny))
                queue.append((nx, ny, step+1))
    
