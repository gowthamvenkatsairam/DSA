class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        arr = [0] * k
        self.min_diff = float("inf")
        def findUnfair(idx):
            if max(arr) >= self.min_diff:
                return
            if idx == n:
                self.min_diff = min(self.min_diff, max(arr))
                return
            for i in range(k):
                arr[i] += cookies[idx]
                findUnfair(idx+1)
                arr[i] -= cookies[idx]
        findUnfair(0)
        return self.min_diff



        