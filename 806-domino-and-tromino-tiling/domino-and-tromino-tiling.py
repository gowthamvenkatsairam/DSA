class Solution:
    def numTilings(self, n: int) -> int:
        dp = {}
        mod = 10 ** 9 + 7
        def f(col, state):
            if col == n:
                return 1 if state == 0 else 0
            if col > n:
                return 0
            if (col, state) in dp: return dp[(col,state)]
            ways = 0
            if state == 0:
                ways = f(col + 1, 0) + f(col + 2, 0) + f(col + 1, 1) + f(col + 1, 2)
            elif state == 1:
                ways = f(col + 1, 2) + f(col + 2, 0)    
            else:
                ways = f(col + 2, 0) + f(col + 1, 1)  
            dp[(col, state)] = ways % mod
            return dp[(col, state)]
        return f(0, 0)
        
        