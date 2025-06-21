"""

Lowest common ancestor of a tree 

"""

def lca(node, p, q):
    if not node or node == p or node == q:
        return node
    left = lca(node.left, p ,q)
    right = lca(node.right, p, q)
    if left and right: return node
    return left or right