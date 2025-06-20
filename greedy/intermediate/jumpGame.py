"""

Jump game problem 1

"""

def canJump(nums):
    farthest = 0
    for start, num in nums:
        if start > farthest:
            return False
        farthest = max(farthest, start+num)
    
    return True
