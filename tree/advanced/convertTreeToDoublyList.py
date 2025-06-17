"""

Convert a binary tree to a doubly linked list

"""

def treeToDoublyLinkedList(root):
    
    if not root:
        return None
    first = last = None
    def dfs(node):
        if not node: return
        dfs(node.left)
        if last:
            last.right = node
            node.left = last
        else:
            first = node
        last = node
        dfs(node.right)
        
    
    dfs(root)
    first.left = last
    last.right = first
    return first
