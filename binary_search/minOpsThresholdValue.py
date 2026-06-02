class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        first = 0
        last = len(nums)-1
        while first < last:
            mid = (first+last)//2
            if nums[mid] >= k:
                last = mid
            else:
                first = mid + 1
        return first 