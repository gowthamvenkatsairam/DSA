class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # def f(i, j, moves):
        #     if not (0 <= i < n and 0 <= j < n):
        #         return 0
        #     if moves == k:
        #         return 1
        #     dx = [-2, 2, 2, -2, -1, 1, 1, -1]
        #     dy = [1, 1, -1, -1, 2, 2, -2, -2]
        #     prob = 0
        #     for l in range(8):
        #         ni, nj = i + dx[l], j + dy[l]
        #         prob += (1 / 8) * f(ni, nj, moves+1)
        #     return prob
        # return f(row, column, 0) 

        dp = {}
        def f(i, j, moves):
            if not (0 <= i < n and 0 <= j < n):
                return 0
            if moves == k:
                return 1
            if (i, j, moves) in dp: return dp[(i, j, moves)]
            dx = [-2, 2, 2, -2, -1, 1, 1, -1]
            dy = [1, 1, -1, -1, 2, 2, -2, -2]
            prob = 0
            for l in range(8):
                ni, nj = i + dx[l], j + dy[l]
                prob += (1 / 8) * f(ni, nj, moves+1)
            dp[(i, j, moves)] = prob
            return dp[(i, j, moves)]
        return f(row, column, 0) 

        