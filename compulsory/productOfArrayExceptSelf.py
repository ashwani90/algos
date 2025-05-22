'''

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

def productExceptSelf(nums):

    # get suffix and prefix producr and rhen multiply

    # leave the number you ate currently att

    prefix_prod = [1] * len(nums)
    for i in range(1, len(nums)):
        prefix_prod[i] = nums[i-1]*prefix_prod[i-1]
    print(prefix_prod)

    suffix_prod = [1] * len(nums)
    for i in range(len(nums)-2, -1, -1):
        suffix_prod[i] = nums[i+1]*suffix_prod[i+1]
    print(suffix_prod)

    final_prod = []
    for i in range(len(nums)):
        final_prod.append(prefix_prod[i]*suffix_prod[i])
    
    return final_prod