class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        cookies.sort(reverse = True)
        arr = [0] * k
        self.min_diff = sum(cookies)
        def findUnfair(idx):
            if max(arr) >= self.min_diff:
                return
            if idx == n:
                self.min_diff = min(self.min_diff, max(arr))
                return
            for i in range(k):
                if arr[i] + cookies[idx] >= self.min_diff:
                    continue
                arr[i] += cookies[idx]
                findUnfair(idx+1)
                arr[i] -= cookies[idx]
                if arr[i] == 0:
                    break
        findUnfair(0)
        return self.min_diff



        