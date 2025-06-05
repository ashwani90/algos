"""

Previous smaller element
Use increasing stack

"""

def prev_smaller(nums):
    res = []
    stack = []
    for num in nums:
        while stack and stack[-1] >= num:
            stack.pop()
        
        res.append(stack[-1] if stack else -1)
        stack.append(num)
    
    return res