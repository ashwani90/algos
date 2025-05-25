'''

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1

n = 1 - ans = 1
n = 2 - ans = 2
n = 3 - ans = 5


'''



def dominoAndTromino(n):
    # been told that this is dynamic type problem
    mod = int(1e9 + 7)
        
    def dominoes(i, n, possible):
        if i == n:
            return 0 if possible else 1
        if i > n:
            return 0
        if possible:
            return (dominoes(i + 1, n, False) + dominoes(i + 1, n, True)) % mod
        return (dominoes(i + 1, n, False) + dominoes(i + 2, n, False) + 2 * dominoes(i + 2, n, True)) % mod
    
    return dominoes(0, n, False)