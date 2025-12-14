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

        first = [1, 0, 0]
        second = [0, 0, 0]
        mod = 10 ** 9 + 7
        for col in range(n-1, -1, -1):
            curr = [0, 0, 0]
            curr[0] = (first[0] + first[1] + first[2] + second[0]) % mod
            curr[1] = (first[2] + second[0]) % mod
            curr[2] = (second[0] + first[1]) % mod
            second = first
            first = curr
        return first[0]


        
        