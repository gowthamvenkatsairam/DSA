class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[-1] * (target+1) for _ in range(n+1)]
        def f(dice, total):
            if total > target:
                return 0
            if dice == n:
                 return 1 if total == target else 0
            if dp[dice][total] != -1:
                return dp[dice][total]
            ways = 0
            for face in range(1, k+1):
                ways += f(dice + 1, total + face)
            dp[dice][total] = ways % mod
            return dp[dice][total]
        return f(0, 0)


            
        