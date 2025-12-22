class Solution:
    def countArrangement(self, n: int) -> int:
        used = [0] * (n+1)
        def countWays(idx):
            if idx == n+1:
                return 1
            cnt = 0
            for num in range(1, n+1):
                if (num % idx == 0 or idx % num == 0) and used[num] == 0:
                    used[num] = 1
                    cnt += countWays(idx + 1)
                    used[num] = 0
            return cnt
        return countWays(1)
        