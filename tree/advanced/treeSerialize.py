"""

Tree serialize and deserialize

"""

class TreeDec:

    def serialize(self, node):
        def dfs(node):
            if not node:
                return '#'
            return [str(node.val)] + dfs(node.left) + dfs(node.right)
        return ",".join(dfs(node))
    
    def deserialize(self, dstr):
        vals = iter(dstr.split(","))
        def dfs():
            val = next(vals)
            if val == '#': return
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
