'''

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1

'''

def kthSmallest(n, k):
    def count_prefix(prefix, n):
        count = 0
        curr = prefix
        next_prefix = prefix + 1
        while curr<=n:
            count += min(n+1, next_prefix)-curr
            curr *= 10
            next_prefix *= 10
        return count

    curr = 1
    k -= 1
    while k > 0:
        count = count_prefix(curr, n)
        if count <= k:
            k -= count
            curr += 1
        else:
            curr *= 10
            k -= 1
    return curr