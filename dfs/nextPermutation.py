class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                point = i-1
                break
        else:
            return nums.reverse()
        
        swap = len(nums)-1
        while nums[swap] <= nums[point]:
            swap -= 1
        nums[swap], nums[point] = nums[point], nums[swap]
        nums[point+1:] = reversed(nums[point+1:])
        return nums
        