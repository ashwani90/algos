"""

Convert a tree to a linked list

"""

def flatten(root):
    def dfs(node):
        if not node: return None
        left_tail = dfs(node.left)
        right_tail = dfs(node.right)
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        return right_tail or left_tail or node
    dfs(root)
