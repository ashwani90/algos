'''
Example 2: Longest Common Subsequence (LCS)
Problem:
Given two strings text1 and text2, return the length of their longest common subsequence. 
A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.

'''

def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Fill the DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

'''

Steps:
Define the DP State:

Let dp[i][j] represent the length of the LCS of text1[0..i-1] and text2[0..j-1].

Base Case:

If either string is empty, the LCS is 0. So, dp[0][j] = 0 and dp[i][0] = 0.

Recurrence Relation:

If text1[i-1] == text2[j-1], then dp[i][j] = dp[i-1][j-1] + 1.

Else, dp[i][j] = max(dp[i-1][j], dp[i][j-1]).

Fill the DP Table:

Use nested loops to fill the table row by row.

Extract the Solution:

The answer is dp[m][n], where m and n are the lengths of text1 and text2.
'''