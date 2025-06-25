"""

Path sum from root and leaf

"""

def hasPathSum(root, target_sum):
    if not root: return False
    if not root.left and not root.right:
        return root.val == target_sum
    return (
        hasPathSum(root.left, target_sum-root.left),
        hasPathSum(root.right, target_sum-root.right)
    )