"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        inorder(root)
        def generateBst(left, right):
            if left > right:
                return
            
            mid = (left+right)//2
            node = TreeNode(vals[mid])
            node.left = generateBst(left, mid-1)
            node.right = generateBst(mid+1, right)
            return node
        
        return generateBst(0, len(vals)-1)

