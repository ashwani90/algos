"""

Lexicographical numbers

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]

"""

def lexicographicalNumbers(n):
    res = []

    def dfs(cu):
        if cu > n:
            return
        res.append(cu)
        
        for i in range(10):
            tmp = cu*10 + i
            dfs(tmp)
    for j in range(1, 10):
        dfs(j)
    return res