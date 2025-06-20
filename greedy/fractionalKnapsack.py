"""


Fractional knapsack problem

"""


def fractionalKnapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    for w, v in items:
        if capacity > w:
            capacity = capacity - w
            total_value += v
        else:
            total_value += (v/w)*capacity
            break
    
    return total_value