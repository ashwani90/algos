"""

Solve a maze problem in backtrack usage

"""

def is_valid(maze, x, y, visited):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 1 and not visited[x]

def solve_maze(maze, x, y, path, visited):
    if (x, y) == (len(maze)-1, len(maze[0])-1):
        path.append((x,y))
        return True
    
    if not is_valid(maze, x, y, visited):
        return False
    
    visited[x][y] = True
    path.append((x,y))
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        if solve_maze(maze, x+dx, y+dy, path, visited):
            return True
        
    
    path.pop()
    visited[x][y] = False
    return False