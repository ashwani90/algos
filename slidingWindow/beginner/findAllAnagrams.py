"""
Problem: Find all start indices of p's anagrams in s.

"""

def find_anagrams(s, p):
    res = []
    p_count = Counter(p)
    s_count = Counter()

    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= len(p):
            s_count[s[i - len(p)]] -= 1
            if s_count[s[i - len(p)]] == 0:
                del s_count[s[i - len(p)]]
        if s_count == p_count:
            res.append(i - len(p) + 1)
    return res