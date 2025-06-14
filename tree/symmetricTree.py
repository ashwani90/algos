"""

Symmetric tree

"""

def is_symmetric(root):
    def is_mirror(s1, s2):
        if not s1 and not s2: return True
        if not s1 or not s2 or s1.val != s2.val: return False

        return is_mirror(s1.left, s2.right) and is_mirror(s1.right, s2.left)