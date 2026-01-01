class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        vis = [[0] * n for _ in range(m)]
        islands = 0
        def dfs(i, j):
            vis[i][j] = 1
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1" and vis[ni][nj] != 1:
                    dfs(ni, nj)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and vis[i][j] != 1:
                    dfs(i, j)
                    islands += 1
        return islands
                    
        


        