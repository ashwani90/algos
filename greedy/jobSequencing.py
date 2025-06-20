"""

Job sequencing problem and its solution

"""

def jobSequencing(jobs, deadline):
    obs.sort(key=lambda x: x[1], reverse=True)
    max_deadline = max(job[0] for job in jobs)
    slots = [False]*max_deadline

    profit = 0
    for deadline, profit_value in jobs:
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[i] >= deadline:
                slots[i] = True
                profit += profit_value
                break
    
    return profit