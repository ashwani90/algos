"""

N-Queens problem 
Backtracking solution

"""

def solve_n_queens_until(board, row, n, result):
    if row == n:
        result.append(["".join(r) for r in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens_until(board, row+1, n, result)
            board[row][col] = '.'

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    i, j = row-1, col-1
    while i>= 0 and j>= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    i,j = row-1, col-1
    while i>=0 and j<n:
        if board[i][j] == 'Q':
            return False
        i-= 1
        j+=1
    
    return True

def nQueens(n):
    board = [['.']*n for _ in range(n)]
    result = []
    solve_n_queens_until(board,0,n,result)
    return result