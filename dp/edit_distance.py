'''

Example 3: Edit Distance
Problem:
Given two strings word1 and word2, find the minimum number of operations (insert, delete, or replace) required to convert word1 to word2.

Steps:
Define the DP State:

Let dp[i][j] represent the minimum number of operations to convert word1[0..i-1] to word2[0..j-1].

Base Case:

If word1 is empty, the number of operations is the length of word2 (insert all characters).

If word2 is empty, the number of operations is the length of word1 (delete all characters).

Recurrence Relation:

If word1[i-1] == word2[j-1], then dp[i][j] = dp[i-1][j-1] (no operation needed).

Else, dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) (choose the minimum of insert, delete, or replace).

Fill the DP Table:

Use nested loops to fill the table row by row.

Extract the Solution:

The answer is dp[m][n], where m and n are the lengths of word1 and word2.

'''

def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Base cases
    for i in range(m+1):
        dp[i][0] = i  # Delete all characters
    for j in range(n+1):
        dp[0][j] = j  # Insert all characters
    
    # Fill the DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]