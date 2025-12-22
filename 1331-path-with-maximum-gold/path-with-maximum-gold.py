class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        vis = [[0] * n for _ in range(m)]
        def collectMaxgold(i, j):
            max_gold = 0
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != 0 and vis[ni][nj] == 0:
                    vis[ni][nj] = 1
                    max_gold = max(max_gold, collectMaxgold(ni, nj))
                    vis[ni][nj] = 0
            return max_gold + grid[i][j]
            
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    vis[i][j] = 1
                    ans = max(ans, collectMaxgold(i, j))
                    vis[i][j] = 0
        return ans
            
            
            
                
            
