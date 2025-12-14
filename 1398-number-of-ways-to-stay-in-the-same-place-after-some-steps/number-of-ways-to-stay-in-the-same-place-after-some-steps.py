class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        maxpos = min(arrLen - 1, steps)
        dp = {}
        def f(idx, s):
            if not (0 <= idx <= maxpos):
                return 0
            if s == steps:
                return 1 if idx == 0 else 0
            if (idx, s) in dp:
                return dp[(idx, s)]
            ways = f(idx - 1, s+1) + f(idx, s+1) + f(idx + 1, s + 1)
            dp[(idx, s)] = ways % mod
            return dp[(idx, s)]
        return f(0, 0)




        