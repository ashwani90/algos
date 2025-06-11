"""

You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

 

Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.

"""

def clearStars(s):
    heap = []
    deleted = set()

    for i, c in enumerate(s):
        if c == '*':
            ch, idx = heapq.heappop(heap)
            deleted.add(-idx)
        else:
            heapq.heappush(heap, (c, -i))
    
    res = []
    for i, c in enumerate(s):
        if c == '*' or i in deleted: continue
        res.append(c)
    
    return "".join(res)