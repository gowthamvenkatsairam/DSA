class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = {}
        next_map = {
            "a" : ["e"],
            "e" : ["a", "i"],
            "i" : ["a", "e", "o", "u"],
            "o" : ["i", "u"],
            "u" : ["a"]
        }
        def f(idx, prev):
            if idx == n:
                return 1
            if (idx, prev) in dp:
                return dp[(idx, prev)]
            ways = 0
            if not prev:
                for key, value in next_map.items():
                    ways += f(idx+1, key)
            else:
                for next_char in next_map[prev]:
                    ways += f(idx + 1, next_char)
            dp[(idx, prev)] = ways % mod
            return dp[(idx, prev)]
        return f(0, None)

        
        