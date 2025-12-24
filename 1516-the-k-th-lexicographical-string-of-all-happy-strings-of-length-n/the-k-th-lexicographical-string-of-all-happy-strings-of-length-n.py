class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (2 ** (n-1)):
            return ""
        path = []
        self.cnt = 0
        self.ans = None
        def generateStrings(idx):
            if self.ans != None:
                return
            if idx == n:
                self.cnt += 1
                if self.cnt == k:
                     self.ans = "".join(path)
                return
            for ch in ('a','b','c'):
                if idx-1 >= 0 and ch == path[idx-1]:
                    continue
                path.append(ch)
                generateStrings(idx+1)
                path.pop()
        generateStrings(0)
        return self.ans
            

        