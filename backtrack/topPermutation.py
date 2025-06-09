"""

Toy permutation problem

"""

def backtrack(path, used, toys, result):
    if len(path) == len(toys):
        result.append(path[:])
        return
    
    for i in range(len(toys)):
        if used[i]:
            continue
        
        used[i] = True
        path.append(toys[i])
        backtrack(path, used, toys, result)
        path.pop()
        used[i] = False
    

def all_toy_orders(toys):
    result = []
    used = [False]*len(toys)
    backtrack([], used, toys, result)
    return result