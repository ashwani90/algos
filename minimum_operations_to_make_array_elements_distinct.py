'''

You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:

Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.

 

Example 1:

Input: nums = [1,2,3,4,2,3,3,5,7]

Output: 2

Explanation:

In the first operation, the first 3 elements are removed, resulting in the array [4, 2, 3, 3, 5, 7].
In the second operation, the next 3 elements are removed, resulting in the array [3, 5, 7], which has distinct elements.
Therefore, the answer is 2.

'''

def minimumOperations(self, nums: List[int]) -> int:
    from collections import Counter
    freq = Counter(nums)

    def is_distinct():
        return all(v <= 1 for v in freq.values())

    if is_distinct():
        return 0

    k = 0
    while nums:
        if len(nums) < 3:
            return k + 1

        for i in range(3):
            freq[nums[i]] -= 1
            if freq[nums[i]] == 0:
                del freq[nums[i]]
        nums = nums[3:]
        k += 1
        if is_distinct():
            return k

    return k