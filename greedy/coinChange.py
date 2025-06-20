"""


Coin change problem

"""

def coinChange(coins, amount):
    coins.sort(reverse=True)
    count = 0

    for c in coins:
        while amount >= c:
            amount -= c
            count += 1
    
    return count