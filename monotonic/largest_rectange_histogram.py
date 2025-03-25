'''
Example 2: Largest Rectangle in a Histogram
Problem:
Given an array heights representing the heights of bars in a histogram, find the area of the largest rectangle that can be formed.

Steps:
Use a monotonic increasing stack (elements in the stack are in increasing order).

Iterate through the array:

While the stack is not empty and the current height is less than the height at the top of the stack, pop from the stack and calculate the area of the rectangle.

Push the current index onto the stack.

After the iteration, handle any remaining elements in the stack.

'''


def largestRectangleArea(heights):
    stack = []
    max_area = 0
    n = len(heights)
    
    for i in range(n):
        while stack and heights[i] < heights[stack[-1]]:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            area = heights[top] * width
            max_area = max(max_area, area)
        stack.append(i)
    
    while stack:
        top = stack.pop()
        width = n if not stack else n - stack[-1] - 1
        area = heights[top] * width
        max_area = max(max_area, area)
    
    return max_area