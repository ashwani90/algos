"""

Invert a binary tree

"""

def invertBinary(root):
    if not root: return None

    root.left, root.right = invertBinary(root.right), invertBinary(root.left)
    return root