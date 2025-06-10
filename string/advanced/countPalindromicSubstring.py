"""

Count palindromic substrings

do it in O(n) time

"""

def countPlaindromic(s):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0]*n 
    center = right = 0
    count = 0
    for i in range(n):
        mirror = 2*center-i
        if i<right:
            p[i] = min(right-i, p[mirror])
        a,b = i+p[i]+1, i-p[i]-1
        while a<n and b>=0 and t[a]==t[b]:
            p[i] += 1
            a += 1
            b +=1
        
        if i + p[i] > right:
            center, right = i, i+p[i]
        
        count += (p[i]+1)//2
    
    return count

