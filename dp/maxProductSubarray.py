"""

Maximum product subarray problem

"""

def maxProductSum(nums):
    max_so_far = min_so_far = result = nums[0]
    for n in nums[1:]:
        temp_max = max(n, max_so_far*n, min_so_far*n)
        min_so_far = min(n, max_so_far*n, min_so_far*n)
        max_so_far = temp_max
        result = max(result, max_so_far)
    
    return result