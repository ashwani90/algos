"""

Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = 0
        max_val = 0

        def backtrack(i, temp):
            nonlocal max_val, res
            if i == len(nums):
                if temp > max_val:
                    res = 1
                    max_val = temp
                elif temp == max_val:
                    res += 1
                return
            backtrack(i+1, temp)
            temp = temp | nums[i]
            backtrack(i+1, temp)
        
        backtrack(0,0)
        return res
                