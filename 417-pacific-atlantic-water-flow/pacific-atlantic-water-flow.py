class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ao, po = set(), set()
        def dfs(i, j, ocean):
            ocean.add((i, j))
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and heights[ni][nj] >= heights[i][j] and (ni, nj) not in ocean:
                    dfs(ni, nj, ocean)
            
        for i in range(m):
            dfs(i, n-1, ao)
            dfs(i, 0, po)
        for j in range(n):
            dfs(m-1, j, ao)
            dfs(0, j, po)
        return [pos for pos in po if pos in ao]

            




        