"""
split Array into Consecutive Subsequences


"""

from collections import Counter, defaultdict
def is_possible(nums):
    freq = Counter(nums)
    tail = defaultdict(int)
    
    for num in nums:
        if freq[num] == 0:
            continue
        freq[num] -= 1
        if tail[num - 1] > 0:
            tail[num - 1] -= 1
            tail[num] += 1
        elif freq[num+1] > 0 and freq[num+2] > 0:
            freq[num+1] -= 1
            freq[num+2] -= 1
            tail[num+2] += 1
        else:
            return False
    return True
