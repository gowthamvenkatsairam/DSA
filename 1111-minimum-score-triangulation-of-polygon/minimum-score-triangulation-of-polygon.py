class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[-1] * n for _ in range(n)]
        def f(i, j):
            if j - i + 1 < 3:
                return 0
            if dp[i][j] != -1: return dp[i][j]
            min_score = float("inf")
            for k in range(i+1, j):
                score = (values[i] * values[j] * values[k]) + f(i, k) + f(k, j)
                min_score = min(min_score, score)
            dp[i][j] = min_score
            return dp[i][j]
        return f(0, n - 1)

             