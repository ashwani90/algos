"""

132 pattern problem and its solution

"""

def pattern(num):
    stack = []
    s3 = float("-inf")

    for num in reversed(num):
        if num < s3:
            return True 
        while stack and stack[-1] < num:
            s3 = stack.pop()
        stack.append(num)
    
    return False