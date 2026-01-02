class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m ,n = len(maze), len(maze[0])
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        vis = [[0] * n for _ in range(m)]
        dq = deque([(entrance[0], entrance[1], 0)])
        vis[entrance[0]][entrance[1]] = 1
        while dq:
            i, j, steps = dq.popleft()
            if [i, j] != entrance and (i == 0 or j == 0 or i == m-1 or j == n-1):
                return steps
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and vis[ni][nj] == 0 and maze[ni][nj] == ".":
                    vis[ni][nj] = 1
                    dq.append((ni, nj, steps + 1))
        return -1
        



        