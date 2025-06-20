"""

gas station and gas trip

"""

def gasStation(gas, cost):
    total, curr, start = 0, 0, 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]
        curr = gas[i] - cost[i]
        if curr < 0:
            total_value = 0
            start = i
    
    return start if total >= 0 else -1