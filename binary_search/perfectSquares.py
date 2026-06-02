"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for target in range(1, n + 1):

            for sq in squares:

                if sq > target:
                    break

                dp[target] = min(
                    dp[target],
                    dp[target - sq] + 1
                )

        return dp[n]