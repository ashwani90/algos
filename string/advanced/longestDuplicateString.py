"""

Longest duplucate string

find longest substring that appears at least twice

"""

def longest_dup_substring(s):
    mod = 2**63-1
    base = 256

    def check(L):
        h = 0
        seen = set()
        for i in range(L):
            h = (h*base+ord(s[i]))%mod
        seen.add(h)
        baseL = pow(base, L, mod)

        for start in range(1, len(s)-L+1):
            h = (h*base-ord(S[start-1])*baseL+ord(s[start+L-1]))%mod
            if h in seen:
                return start
            seen.add(h)
        return -1
    
    left, right = 1, len(s)
    start = -1
    while left<= right:
        mid = (left+right)//2
        idx = check(mid)
        if idx != -1:
            left = mid + 1
            start = idx
        else:
            right = mid - 1
    
    return "" if start == -1 else s[start:start+left-1]