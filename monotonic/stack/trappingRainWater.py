"""

Trapping rain water problem

"""

def trapRainWater(height):
    stack = []
    res = 0

    for i in range(len(height)):
        while stack and height[stack[-1]] < height[i]:
            top = stack.pop()
            if not stack:
                break
            dist = i - stack[-1]-1
            bounded = min(height[i], height[stack[-1]]) - height[top]
            res += dist*bounded
        
        stack.append(i)
    
    return res