"""
Binary lifting of a ancestor

"""

LOG = 16  # For trees with up to 2^16 nodes

class TreeAncestor:
    def __init__(self, n, parent):
        self.dp = [[-1]*LOG for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
        for j in range(1, LOG):
            for i in range(n):
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def get_kth_ancestor(self, node, k):
        for j in range(LOG):
            if k & (1 << j):
                node = self.dp[node][j]
                if node == -1:
                    break
        return node
