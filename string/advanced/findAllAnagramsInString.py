"""

Find all anagrams in a string
find all start indices of p's anagrams in s

"""

from collections import Counter

def find_anagrams(s, p):

    p_count = Counter(p)
    s_count = Counter(s)
    res = []
    left = 0

    for right in range(len(s)):
        s_count[s[right]] += 1
        if right-left+1 > len(p):
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1
        if s_count == p_count:
            res.append(left)
    
    return res
