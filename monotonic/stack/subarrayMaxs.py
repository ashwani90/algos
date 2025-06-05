"""

Sum of subarray maximums

"""

def sumMaxSubarray(arr):
    res, mod = 0, 10**9+7

    stack = []
    for i in range(len(arr)+1):
        cur = arr[i] if i < len(arr) else float('inf')
        while stack and arr[stack[-1]] < cur:
            j = stack.pop()
            k = stack[-1] if stack else -1
            res += arr[j] * (i-j) * (j-k)
        stack.append(i)
    
    return res%mod