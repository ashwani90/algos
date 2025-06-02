'''

You are given an integer array nums and an integer k.

An integer h is called valid if all values in the array that are strictly greater than h are identical.

For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.

You are allowed to perform the following operation on nums:

Select an integer h that is valid for the current values in nums.
For each index i where nums[i] > h, set nums[i] to h.
Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.

 

Example 1:

Input: nums = [5,2,5,4,5], k = 2

Output: 2

Explanation:

The operations can be performed in order using valid integers 4 and then 2.

Example 2:

Input: nums = [2,1,2], k = 2

Output: -1

Explanation:

It is impossible to make all the values equal to 2.

'''

def minOperations(nums):
     if k > min(nums):
            return -1

        # Step 2: Count the number of unique elements in the list by converting it to a set.
        # Converting the list to a set removes duplicates, leaving us with only unique elements.
        unique_elements = set(nums)
        unique_count = len(unique_elements)

        # Step 3: If 'k' is already in the list, return the number of unique elements minus 1.
        # No operation is needed to reach 'k', so we subtract 1 from the unique count.
        if k in unique_elements:
            return unique_count - 1
        else:
            # Step 4: If 'k' is not in the list, return the number of unique elements.
            # In this case, we must perform at least one operation for each unique element in the list.
            return unique_count