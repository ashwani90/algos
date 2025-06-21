"""

Right side biew of a tree

"""

from collections import deque

def right_side_view(root):
    if not root: return []
    result = []
    queue = deque([root])
    while queue:
        size = len(queue)
        for i  in range(size):
            node = queue.popleft()
            if i == size - 1:
                result.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    
    return result