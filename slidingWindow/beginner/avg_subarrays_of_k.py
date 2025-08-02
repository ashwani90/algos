"""
Problem: Return an array with averages of all contiguous subarrays of size k.
"""

def avg_subarrays_of_k(arr, k):
    res = []
    window_sum = sum(arr[:k])
    res.append(window_sum/k)

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        res.append(window_sum/k)
    return res