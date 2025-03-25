'''
Example 1: Next Greater Element
Problem:
Given an array nums, return an array ans where ans[i] is the next greater element for nums[i]. If no such element exists, set ans[i] = -1.

Steps:
Use a monotonic decreasing stack (elements in the stack are in decreasing order).

Iterate through the array:

While the stack is not empty and the current element is greater than the top of the stack, pop from the stack and set ans[top] = current element.

Push the current element onto the stack.

After the iteration, any remaining elements in the stack have no next greater element, so set their ans values to -1.

'''

def nextGreaterElement(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            top = stack.pop()
            ans[top] = nums[i]
        stack.append(i)
    
    return ans