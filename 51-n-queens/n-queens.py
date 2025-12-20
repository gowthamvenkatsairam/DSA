class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def getWays(idx, board, top_left, top_right, top):
            if idx == n:
                result.append(["".join(row) for row in board])
                return
            for col in range(n):
                valid = True
                if idx - col in top_left: valid = False
                if idx + col in top_right: valid = False
                if col in top: valid = False
                if valid:
                    board[idx][col] = "Q"
                    top_left.add(idx - col)
                    top_right.add(idx + col)
                    top.add(col)
                    getWays(idx + 1, board, top_left, top_right, top)
                    top_left.remove(idx - col)
                    top_right.remove(idx + col)
                    top.remove(col)
                    board[idx][col] = "."
        board = [["."] * n for _ in range(n)]
        getWays(0, board, set(), set(), set())
        return result
                    




        