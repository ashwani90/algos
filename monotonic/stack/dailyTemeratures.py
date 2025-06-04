"""

Daily temperatures problem

"""

def warmerDay(temps):
    res = [0]*len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            j = stack.pop()
            res[j] = i-j
        stack.append(i)
    
    return res