"""

Given an array, build a Fenwick Tree and find the prefix sum up to index i.

"""

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i 
    
    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i 
        
        return s

arr = [1,2,3,4,5]
ft = FenwickTree(len(arr))
for idx, val in enumerate(arr, 1):
    ft.update(idx, val)

print(ft.prefix_sum(3))


# Range sum query using fenwuck query
def range_sum(ft, l, r):
    return ft.prefix_sum(r) - ft.prefix_sum(l-1)

print(range_sum(ft, 2, 4))


#  Update Value in Array and Fenwick Tree

