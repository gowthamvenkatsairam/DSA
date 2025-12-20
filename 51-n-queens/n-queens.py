class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        top_left, top_right, top = set(), set(), set()
        result = []
        def getWays(idx):
            if idx == n:
                result.append(["".join(row) for row in board])
                return
            for col in range(n):
                if idx - col in top_left or idx + col in top_right or col in top:
                    continue
                board[idx][col] = "Q"
                top_left.add(idx - col)
                top_right.add(idx + col)
                top.add(col)
                getWays(idx + 1)
                top_left.remove(idx - col)
                top_right.remove(idx + col)
                top.remove(col)
                board[idx][col] = "."
        getWays(0)
        return result
                    




        