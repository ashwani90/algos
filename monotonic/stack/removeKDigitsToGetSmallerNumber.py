"""

Remove k digits to get smaller number

"""

def remove_k_digits(num, k):
    stack = remove_k_digits
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    final = stack[:-k] if k else stack
    return ''.join(final).lstrip('0') or '0'