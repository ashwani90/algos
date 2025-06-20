"""
Mazimum sum after k negations

"""

def maxSum(nums):
    nums.sort(reverse=True)
    for i in range(len(nums)):
        if k >0 and nums[i] < 0:
            k -= 1
            nums[i] = -nums[i]

    if k % 2 == 1:
        nums.sort()
        nums[0] = -nums[0]

    return sum(nums)   