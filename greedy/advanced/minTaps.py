"""
Min taps that needs to be opened

"""

def min_taps(n, ranges):
    intervals = [(max(0, i - r), min(n, i + r)) for i, r in enumerate(ranges)]
    intervals.sort(reverse=True)
    end, farthest, taps, i = 0,0,0,0
    while end < n:
        while i < len(intervals) and intervals[i][0] <= end:
            farthest = max(farthest, intervals[i][1])
            i += 1
        
        if farthest == end:
            return -1
        
        end = farthest
        taps += 1
    
    return taps