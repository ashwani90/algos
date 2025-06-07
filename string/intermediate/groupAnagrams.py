
"""

group anagrams problem

"""

from collections import Counter

def groupAnagrams(strs):
    groups =  defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(group.values())