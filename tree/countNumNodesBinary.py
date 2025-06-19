"""

Count number of nodes in a binary tree

"""

def countNodes(node):
    if not node:
        return 0
    return 1 + countNodes(node.left) + countNodes(node.right)