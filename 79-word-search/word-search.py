class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        vis = [[0] * n for _ in range(m)]
        dir = {(-1, 0), (0, 1), (1, 0), (0, -1)}
        self.found = False
        def findWord(i, j, idx):
            if idx == len(word):
                self.found = True
                return
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[idx] and vis[ni][nj] == 0:
                    vis[ni][nj] = 1
                    findWord(ni, nj, idx + 1)
                    vis[ni][nj] = 0

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and self.found == False:
                    vis[r][c] = 1
                    findWord(r, c, 1)
                    vis[r][c] = 0
        return self.found



        