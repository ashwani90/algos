'''

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

'''

# this works on leet code so I do not care about the voting algo

from collections import Counter
def majorityElement2(nums):
    nlen = len(nums)

    k = nlen//3
    counts = Counter(nums)
    res = []
    for i, j in counts.items():
        if j > k:
            res.append(i)
    
    return res
