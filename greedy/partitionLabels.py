"""

Partition labels
"""

def partition_labels(string):
    last = {c:i for i,c in enumerate(string)}
    res = []
    for i, c in enumerate(string):
        end = max(end, last[c])
        if i == end:
            res.append(end-start+1)
            start = i + 1
    
    return res