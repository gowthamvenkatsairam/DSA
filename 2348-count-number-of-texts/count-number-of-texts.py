class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10 ** 9 + 7
        n = len(pressedKeys)
        dp = [-1] * n
        def countMessages(idx):
            if idx > n:
                return 0
            if idx == n:
                return 1
            if dp[idx] != -1: return dp[idx]
            cnt = 0
            max_presses = 4 if pressedKeys[idx] in ("7", "9") else 3
            for j in range(1, max_presses + 1):
                if idx + j < n and pressedKeys[idx + j] != pressedKeys[idx]:
                    cnt += countMessages(idx + j)
                    break
                cnt += countMessages(idx + j)
            dp[idx] = cnt % mod
            return dp[idx]
        return countMessages(0)

        