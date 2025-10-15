class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])  
        MOD = 10**9+7
        
        directions = [(0,1), (1,0)]
        queue = deque([(0, 0, grid[0][0])])  # (row, col, distance)
        i = 0
        
        while queue:
            r, c, dist = queue.popleft()
            if r == m-1 and c == n-1:
                if dist % k == 0:
                    i = ((i + 1) % MOD)
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    queue.append((nr, nc, dist+grid[nr][nc]))
        return i