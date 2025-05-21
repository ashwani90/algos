'''

Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.

'''

from collections import Counter
def mostFrequentEvenElement(nums):

    counts = Counter(nums)
    res = -1
    maxOccur = 0
    for i, j in counts.items():
        if i%2 == 0 and j >= maxOccur:
            if i < res and j == maxOccur:
                res = i 
                maxOccur = j
            elif i > res and j == maxOccur:
                continue
            else:
                res = i 
                maxOccur = j
    
    return res