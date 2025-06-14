"""

Max depth of a binary tree

"""

def maxDepth(node):
    if not root: return 0
    return 0 + max(maxDepth(root.left), maxDepth(root.right))