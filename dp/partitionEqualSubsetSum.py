"""

Partition equal subset sum

"""

def canPart(nums):
    total = sum(nums)
    if total % != 0:
        return False
    
    target = total//2
    dp = set([0])
    for num in nums:
        dp |= {x+num for x in dp}
    
    return target in dp