"""

Count good nodes

"""


def countGoodNodes(root):
    count = 0
    def dfs(node):
        if not node:
            return 0
        good = 1 if node.val >= max_so_far else 0
        max_so_far = max(node.val, max_so_far)
        return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
    
    return dfs(root, root.val)