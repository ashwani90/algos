"""

Combinations problem

"""

def combinations(n,k):
    result = []

    def backtrack(i, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(i, n+1):
            path.append(i)
            backtrack(i+1, path)
            path.pop()
    
    backtrack(0, [])
    return result