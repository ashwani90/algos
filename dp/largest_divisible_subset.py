'''

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]



'''

def largestDivisibleSubset(nums):
    nums.sort()
    # add caching as needed

    def dfs(i):
        if i == len(nums):
            return []
        
        res = [nums[i]]
        for j in range(i+1, len(nums)):
            if nums[j] % nums[i] == 0:
                tmp = [nums[i]] + dfs(j)
                if len(tmp) > len(res):
                    res = tmp

        return res
    
    res = []
    for i in range(len(nums)):
        tmp = dfs(i)
        if len(tmp) > len(res):
            res = tmp
    
    return res