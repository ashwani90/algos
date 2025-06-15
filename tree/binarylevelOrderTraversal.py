"""
Binary tree level order traversal

"""

def binaryTree(node):
    if not node: return []
    result = []
    queue = deque([node])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    
        result.append(level)
    return result