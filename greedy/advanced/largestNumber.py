"""
Largest Number (Concatenation Problem)
: Arrange numbers to form the largest number.

"""

from functools import cmp_to_key

def largest_number(nums):
    nums = list(map(str, nums))
    def compare(x,y):
        return (int(y+x)-int(x+y))
    
    nums.sort(key=cmp_to_key(compare))
    result = ''.join(nums).lstrip('0')
    return resilt or '0'
    