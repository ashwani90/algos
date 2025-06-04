"""

Largest rectangle in a histogram

"""

def largestRect(heights):
    stack = []
    max_area = 0

    heights.append(0)

    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, H*W)
        
        stack.append(i)
    
    return max_area