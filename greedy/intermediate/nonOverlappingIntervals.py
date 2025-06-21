"""
Non pverlapping intervals

"""

def nonOverlapping(intervals):
    intervals.sort(key=lambda x: x[1])
    count, end = 0, float('-inf')
    for start, finish in intervals:
        if start < end:
            count += 1
        else:
            end = finish
    return count
