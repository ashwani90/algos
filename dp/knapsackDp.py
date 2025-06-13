"""

Knapsack Problem dp

"""

def knapsack(weights, values, W):
    n = len(values)
    dp = [0]*(W+1)
    for i in range(n):
        for w in range(W, weights[i]-1, -1):
            dp[W] = max(dp[w], wp[w-weights[i]]+values[i])
    
    return dp[W]