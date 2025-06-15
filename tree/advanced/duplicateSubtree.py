"""

Duplicate subtrees check for them

"""

from collections import defaultdict

def find_duplicate_subtrees(root):
    count = defaultdict(int)
    result = []

    def serialize(node):
        if not node: return "#"
        s = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
        count[s] += 1
        if count[s] == 2:
            result.append(node)
        return s

    serialize(root)
    return result
