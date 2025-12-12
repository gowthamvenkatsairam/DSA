class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = {}
        mod = 10 ** 9 + 7
        def f(num, cnt, seq_len):
            if seq_len == n:
                return 1
            if (num, cnt, seq_len) in dp:
                return dp[(num, cnt, seq_len)]
            seq_cnt = 0
            for i in range(6):
                idx = i + 1
                if idx != num:
                    seq_cnt += f(idx, 1, seq_len+1)
                elif idx == num and cnt < rollMax[idx-1]:
                    seq_cnt += f(idx, cnt + 1, seq_len+1)
            dp[(num, cnt, seq_len)] = seq_cnt % mod
            return dp[(num, cnt, seq_len)]
        ans = 0
        for i in range(6):
            ans += f(i+1, 1, 1)
        return ans % mod
