"""
Min deletion to make character frequencies unique

Given a string, remove the minimum number of characters so that no two characters have the same frequency.


"""
from collections import Counter
def min_deletions(s):
    counts = Counter(s)
    used = set()
    deletion = 0

    for c, i in counts.items():
        while c in used and c > 0:
            c -= 1
            deletion += 1
            # Think this is wrong
        used.add(i)
    
    return deletion