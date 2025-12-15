class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[-1] * 5 for _ in range(n)]
        next_map = {
            0 : [1],
            1 : [0, 2],
            2 : [0, 1, 3, 4],
            3 : [2, 4],
            4 : [0]
        }
        def f(idx, prev):
            if idx == n:
                return 1
            if dp[idx][prev] != -1:
                return dp[idx][prev]
            ways = 0
            for next_char in next_map[prev]:
                ways += f(idx + 1, next_char)
            dp[idx][prev] = ways % mod
            return dp[idx][prev]
        result = 0
        for i in range(5):
            result += f(1, i)
        return result % mod

        
        