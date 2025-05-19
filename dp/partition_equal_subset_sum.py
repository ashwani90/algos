'''

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is 
equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

'''

def partition_equal_subset_sum(nums):
    target = sum(nums)//2

    if sum(nums)%2:
        return False

    dp = set()
    dp.add(0)
    
    for i in range(len(nums)-1, -1, -1):
        nextDp = set()
        for t in dp:
            nextDp.add(t+nums[i])
            nextDp.add(t)
        dp = nextDp
    return True if target in dp else False
