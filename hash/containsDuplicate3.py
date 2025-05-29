'''

You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

 

Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.


'''

def containsDuplicate3(nums, indexDiff, valueDiff):
    # Base condition

    if not nums or indexDiff <= 0 or valueDiff < 0:
        return False

    sorted_list = SortedList()
    for i, num in enumerate(nums):
        # Find the smallest value in the sorted list greater than or equal to nums[i] - valueDiff
        min_value = num - valueDiff
        max_value = num + valueDiff
        
        # Check if there's any number within the range [nums[i] - valueDiff, nums[i] + valueDiff]
        pos = sorted_list.bisect_left(min_value)
        if pos < len(sorted_list) and sorted_list[pos] <= max_value:
            return True
        
        # Add the current number to the sorted list
        sorted_list.add(num)

        # Remove numbers that are out of the indexDiff range
        if len(sorted_list) > indexDiff:
            sorted_list.remove(nums[i - indexDiff])

    return False