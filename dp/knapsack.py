"""

Given weights and values if items, chose to include and exclude to maximize value without exceeding weight limit

Knapsack problem write details here
how it works and how to solve it

"""

def knapsack(weights, values, capacity):
    n = len(values)

    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(capacity+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], values[i-1]+dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][capacity]