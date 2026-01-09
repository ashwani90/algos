"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, temp):
            if i == len(nums):
                res.append(temp[:])
                return
            
            temp.append(nums[i])
            backtrack(i+1, temp)
            temp.pop()
            backtrack(i+1, temp)
        
        backtrack(0, [])
        return res