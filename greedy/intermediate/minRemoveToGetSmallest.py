"""
Remove min digits to get the smallest number
"""

def min_num(digits, k):
    stack = []
    for digit in digits:
        while k > 0 and stack and stack[-1] > digit:
            k -= 1
            stack.pop()
        stack.append(digit)
    
    while k > 0:
        stack.pop()
    
    result = "".join(stack).lstrip("0")
    return result if result else '0'