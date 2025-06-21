"""

Inorder traversal

"""

def inorder(node):
    res = []
    def dfs(node):
        if not node: return True
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return res