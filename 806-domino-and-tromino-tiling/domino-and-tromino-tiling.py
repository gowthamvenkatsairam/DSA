class Solution:
    def numTilings(self, n: int) -> int:
        # dp = {}
        # mod = 10 ** 9 + 7
        # def f(col, state):
        #     if col == n:
        #         return 1 if state == 0 else 0
        #     if col > n:
        #         return 0
        #     if (col, state) in dp: return dp[(col,state)]
        #     ways = 0
        #     if state == 0:
        #         ways = f(col + 1, 0) + f(col + 2, 0) + f(col + 1, 1) + f(col + 1, 2)
        #     elif state == 1:
        #         ways = f(col + 1, 2) + f(col + 2, 0)    
        #     else:
        #         ways = f(col + 2, 0) + f(col + 1, 1)  
        #     dp[(col, state)] = ways % mod
        #     return dp[(col, state)]
        # return f(0, 0)

        dp = [[0] * 3 for _ in range(n+1)]
        dp[n][0] = 1
        mod = 10 ** 9 + 7
        for col in range(n-1, -1, -1):
            for state in range(3):
                if state == 0:
                    dp[col][state] = dp[col+1][0] + dp[col+1][1] + dp[col+1][2] + (dp[col+2][0] if col+2 <= n else 0)
                if state == 1:
                    dp[col][state] = dp[col+1][2] + (dp[col+2][0] if col+2 <= n else 0)
                if state == 2:
                    dp[col][state] = (dp[col+2][0] if col+2 <= n else 0) + dp[col+1][1]
        return dp[0][0] % mod


        
        