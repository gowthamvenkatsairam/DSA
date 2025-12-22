class Solution:
    def countArrangement(self, n: int) -> int:
        dp = {}
        def countWays(idx, mask):
            if idx == n+1:
                return 1
            if (idx, mask) in dp:
                return dp[(idx, mask)]
            cnt = 0
            for num in range(1, n+1):
                if (num % idx == 0 or idx % num == 0) and (mask & (1 << num)) == 0:
                    cnt += countWays(idx + 1, mask | (1 << num))
            dp[(idx, mask)] = cnt
            return dp[(idx, mask)]
        return countWays(1, 0)
        