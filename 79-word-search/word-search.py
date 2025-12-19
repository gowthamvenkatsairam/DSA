class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = [[0] * n for _ in range(m)]
        dir = {(-1, 0), (0, 1), (1, 0), (0, -1)}
        def findWord(i, j, idx):
            if idx == len(word):
                return True
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[idx] and vis[ni][nj] == 0:
                    vis[ni][nj] = 1
                    if findWord(ni, nj, idx + 1):
                        return True
                    vis[ni][nj] = 0
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    vis[r][c] = 1
                    if findWord(r, c, 1):
                        return True
                    vis[r][c] = 0
        return False



        