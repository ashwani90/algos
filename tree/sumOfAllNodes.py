"""

get sum of all nodes in a binary tree

"""


def sumNodes(node):

    if not node:
        return 0
    return node.val + sumNodes(node.left) + sumNodes(node.right)