"""

Path sum 3 problem

"""
from collections import defaultdict

def pathSum(root):
    prefix = defaultdict(int)
    prefix[0] = 1
    def dfs(node, curr_sum):
        if not node: return 0
        curr_sum += node.val
        prefix[curr_sum] += 1
        res = prefix[target-curr_sum]
        res += dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        prefix[curr_sum] -= 1
        return res
    return dfs(root, 0)
