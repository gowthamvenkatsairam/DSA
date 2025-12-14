class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = {}
        mod = 10 ** 9 + 7
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def f(i, j, moves):
            if moves > maxMove:
                return 0
            if not (0 <= i < m and 0 <= j < n):
                return 1
            if (i, j, moves) in dp:
                return dp[(i, j, moves)]
            ways = 0
            for di, dj in dir:
                ni, nj = i + di, j + dj
                ways += f(ni, nj, moves + 1)
            dp[(i, j , moves)] = ways % mod
            return dp[((i, j, moves))]
        return f(startRow, startColumn, 0)
            
        