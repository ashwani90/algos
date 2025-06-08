"""

Solve sudoku problem

"""

def is_valid(board, row, col, num):
    num = str(num)
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_row, box_col = 3 * (row//3), 3*(col//3)
    for i in range(box_row, box_row+3):
        for j in range(box_col, box_col+3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                for num in range(1,10):
                    if is_valid(board, row, col, num):
                        board[row][col] = str(num)
                        if solve_sudoku(board):
                            return True
                        board[row][col] = '.'
                return False
    
    return True
