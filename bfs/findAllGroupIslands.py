"""
You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

"""

class Solution:
    def findFarmland2(self, land: List[List[int]]) -> List[List[int]]:
        if not land or not land[0]:
            return []

        rows, cols = len(land), len(land[0])
        result = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            queue = deque([(r, c)])
            land[r][c] = 0  # mark visited
            min_r, min_c, max_r, max_c = r, c, r, c

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and land[nx][ny] == 1:
                        land[nx][ny] = 0
                        queue.append((nx, ny))
                        max_r = max(max_r, nx)
                        max_c = max(max_c, ny)
            return [r, c, max_r, max_c]

        # Scan all cells
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:
                    result.append(bfs(i, j))

        return result
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        if not land or not land[0]:
            return []


        rows, cols = len(land), len(land[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []

        def bfs(i, j):
            queue = deque([(i, j)])
            land[i][j] = 0  # mark visited
            min_r, min_c, max_r, max_c = i , j, i, j

            # actual bfs logic
            while queue:
                nr, nc = queue.popleft()
                for dr, dc in directions:
                    neir, neic = nr+dr, nc+dc
                    if 0 <= neir < rows and 0 <= neic < cols and land[neir][neic] == 1:
                        queue.append((neir, neic))
                        max_r = max(max_r, neir)
                        max_c = max(max_c, neic)
            return [i, j, max_r, max_c]



        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:
                    result.append(bfs(i, j))
        return result