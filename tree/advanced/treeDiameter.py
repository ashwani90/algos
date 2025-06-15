"""

Tree diameter of a non binary tree

"""

def treeDiameter(root):

    def dfs(node):
        if not node:
            return 0
        max1 = max2 = 0
        for n in node.children:
            h = dfs(n)
            if h > max1:
                max1, max2 = h, max1
            elif h > max2:
                max1, max2 = max1, h 
        res = max(res, max1+max2)
        return 1 + max1
    dfs(root)
    return res