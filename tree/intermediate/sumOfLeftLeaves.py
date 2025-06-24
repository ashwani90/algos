"""

Sum of left leaves

"""

def sumOfLeftLeaves(root):
    if not root: return 0
    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val
    return total + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)
    