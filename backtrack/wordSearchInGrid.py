"""

Word search in a grid problems

like it has a grid and in that we need to search for a word

"""

def wordSearch(board,word):
    
    def backtrack(i,j,k):
        if k == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] != word[k]:
            return False
        
        tmp = board[i][j]
        board[i][j] = '#'

        for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            if backtrack(i+dx,j+dy,k+1):
                return True
        
        board[i][j] = tmp
        # problem with this as it might come back to same index and give problems
        # if word[k] == board[i][j] and backtrack(i-1,j,k) and backtrack(i+1,j,k) and backtrack(i,j-1,k) and backtrack(i,j+1,k):
        #     return True
        return False
    
    for i in range(rows):
        for j in range(cols):
            if backtrack(i,j,0):
                return True
    
    return backtrack(0,0,0)
