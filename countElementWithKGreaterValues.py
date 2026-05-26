class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)
        nums.sort()

        count = 0

        look_for = nums[-k]
        for i in nums:
            if i < look_for:
                count += 1
        return count