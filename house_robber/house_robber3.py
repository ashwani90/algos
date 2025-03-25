'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

'''

def rob(root):
    def dfs(root):
        if not root:
            return (0, 0)
        left = dfs(root.left)
        right = dfs(root.right)
        return (root.val+left[1]+right[1], max(left[0], left[1]) + max(right[0],right[1]))

    return max(dfs(root))

    # Try another solution from neetcode

def rob(root):
    
    def dfs(root):
        if not root:
            return [0,0]

        leftPair = dfs(root.left)
        rightPair = dfs(root.right)

        withRoot = root.val + leftPair[1] + rightPair[1]
        withoutRoot = max(leftPair) + max(rightPair)

        return [withRoot, withoutRoot]
    
    return max(dfs(root))