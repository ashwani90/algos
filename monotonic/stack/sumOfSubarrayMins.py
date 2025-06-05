"""
Problem of sum of subarray mins

"""

def sumSubarraySums(arr):
    stack = []
    res = 0
    arr.append(0)

    for i, num in enumerate(arr):
        while stack and arr[stac[-1]] > num:
            j = stack.pop()
            k = stack[-1] if stack else -1
            res += arr[j] * (i-j) * (k-j)
        stack.append(i)
    
    return res