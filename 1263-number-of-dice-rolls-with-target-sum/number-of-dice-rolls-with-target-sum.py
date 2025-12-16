class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[n][target] = 1
        for dice in range(n-1, -1, -1):
            for total in range(target, -1 , -1):
                ways = 0
                for face in range(1, k+1):
                    ways += (dp[dice + 1][total + face]) if total + face <= target else 0
                dp[dice][total] = ways % mod
        return dp[0][0]






            
        