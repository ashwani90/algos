"""

Next greater element
find next greater element to the right

use a decreasing stack to track elements

"""

def next_greater_element(nums):
    res = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            res[stack.pop()] = nums[i]
        
        stack.append(i)
    
    return res

