class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        vis = [[0] * n for _ in range(m)]
        def countPaths(i, j, unused):
            if grid[i][j] == 2:
                return 1 if unused == -1 else 0
            ways = 0
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != -1 and vis[ni][nj] == 0:
                    unused -= 1
                    vis[ni][nj] = 1
                    ways += countPaths(ni, nj, unused)
                    unused += 1
                    vis[ni][nj] = 0
            return ways

        unused = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_r, start_c = i, j
                elif grid[i][j] == 0:
                    unused += 1
        vis[start_r][start_c] = 1
        return countPaths(start_r, start_c, unused)
        

            
        