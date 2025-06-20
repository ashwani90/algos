"""

Find overlappign activites

sort of time 
and check end_tine and start_time

"""

def overlap_activity(times):
    times = sorted(zip(start, end), key=lambda x: x[1])

    count = 1
    last = times[0][1]
    for i in range(1, len(times)):
        if times[i][0] > last:
            count += 1
            last = times[i][1]
    
    return count