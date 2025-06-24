"""

Build tree from inorder and preorder

"""

def buildTree(inoder, preorder):
    if not inoder or not preorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    idx = inoder.index(root_val)
    root.left = buildTree(preorder[1:idx+1], inorder[:idx])
    root.right = buildTree(preorder[idx+1:], inorder[idx+1:])
    return root
