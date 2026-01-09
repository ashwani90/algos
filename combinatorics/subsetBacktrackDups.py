"""
Same as subsets backtrack but can have duplucates
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # need to do this so as to process numbers sequentially
        res = []

        def backtrack(start, temp):
            res.append(temp[:])   

            for i in range(start, len(nums)):
                # skip duplicates at same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                temp.append(nums[i])
                backtrack(i + 1, temp)
                temp.pop()

        backtrack(0, [])
        return res