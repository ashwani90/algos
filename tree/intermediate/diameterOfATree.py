"""

Get diamatere of a tree

"""


def diameter(root):
    if not root: return 0
    diameter = 0
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left+right)
        return 1 + max(left, right)
    
    dfs(root)
    return diameter