"""

Find first non repeating charatcer

"""
from collections import Counter

def firstNonRepeatingChar(s):

    freq = Counter(s)

    for i in s:
        if freq[i] == 1:
            return i
    
    return -1
