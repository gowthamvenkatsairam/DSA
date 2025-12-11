class Solution:
    def knightDialer(self, n: int) -> int:
        dp = {}
        row ,col = 4, 3
        mod = 10 ** 9 + 7
        def f(i ,j, length):
            if not (0 <= i < row and 0 <= j < col) or (i, j) in {(3, 0), (3, 2)}:
                return 0
            if length == n:
                return 1
            if (i, j, length) in dp:
                return dp[(i, j, length)]
            dx = [-2, 2, 2, -2, -1, 1, 1, -1]
            dy = [1, 1, -1, -1, 2, 2, -2, -2]
            res = 0
            for l in range(8):
                ni, nj = i + dx[l], j + dy[l]
                res += f(ni, nj, length + 1)
            dp[(i, j, length)] = res % mod
            return dp[(i, j, length)]
        ans = 0
        for r in range(row):
            for c in range(col):
                ans += f(r, c, 1)
        return ans % mod


            
            

        