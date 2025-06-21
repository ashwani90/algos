"""

Check if a tree is balanced

"""

def treeBalanced(root):
    def check(node):
        if not node: return 0
        left = check(node.left)
        if left == -1: return -1
        right = check(node.right)
        if right == -1 or abs(left-right) > 1:
            return -1
        return 1 + max(left, right)
    
    return check(root) == -1