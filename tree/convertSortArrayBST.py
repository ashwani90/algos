"""

Convert sorted array to BST

"""

class TreeNode:
    def __init__(self, val): self.val, self.right, self.left = val, None, None

def convertSorted(nums):
    if not nums: return None

    mid = len(nums)//2
    node = TreeNode(nums[mid])
    node.left = convertSorted(nums[:mid])
    node.right = convertSorted(nums[mid+1:])
    return node