"""

Suffic array construction
construct suffix array for a string - all suffixes sorted in a lexographic order

"""

def build_suffix_arrau(s):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    sa = list(range(n))

    while k < n:
        sa.sort(key= lambda x: (rank[x], rank[x+k] if x+k < n else -1))
        tmp = [0]*n 
        for i in range(1, n):
            prev, curr = sa[i-1], sa[i]
            tmp[curr] = tmp[prev]+((rank[prev], rank[prev+k] if prev+k < n else -1) < (rank[curr], rank[curr+k] if curr+k<n else -1))
        rank = tmp
        k <<= 1
    
    return sa