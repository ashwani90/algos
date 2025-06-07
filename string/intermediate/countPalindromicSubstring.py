"""

Count how many substrings of a string are palindromic

"""

def count_substrings(s):
    count = 0 

    def expand_around_center(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
    
    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i+1)
    
    return count