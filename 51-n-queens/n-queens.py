class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def getWays(idx, board):
            if idx == n:
                result.append(["".join(row) for row in board])
                return
            for col in range(n):
                valid = True
                i, j = idx - 1, col - 1
                while 0 <= i < n and 0 <= j < n:
                    if board[i][j] == "Q":
                        valid = False
                        break
                    i -= 1
                    j -= 1
                i, j = idx - 1, col + 1
                while 0 <= i < n and 0 <= j < n:
                    if board[i][j] == "Q":
                        valid = False
                        break
                    i -= 1
                    j += 1
                for i in range(idx):
                    if board[i][col] == 'Q':
                        valid = False
                        break 
                if valid:
                    board[idx][col] = "Q"
                    getWays(idx + 1, board)
                    board[idx][col] = "."
        board = [["."] * n for _ in range(n)]
        getWays(0, board)
        return result
                    




        