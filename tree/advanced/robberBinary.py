"""
Robber in a binary tree

"""


def rob(root):

    def dfs(node):
        if not node:
            return (0, 0)
        left = dfs(node.left)
        right = dfs(node.right)
        withN = node.val + left[1] + right[1]
        withoutN = max(left, right)
        return (withN, withoutN)
    
    return max(dfs(root))