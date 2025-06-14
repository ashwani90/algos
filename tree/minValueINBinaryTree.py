"""
minimum value in a binary tree

"""


def minValueinTree(root):
    if not root:
        return float('inf')
    return min(root.val, minValueinTree(root.left), minValueinTree(root.right))
    