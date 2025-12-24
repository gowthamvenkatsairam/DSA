class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        self.ans = float("-inf")
        used_mentors = [0] * m
        self.score = 0
        computed = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                for k in range(n):
                    if students[i][k] == mentors[j][k]:
                        computed[i][j] += 1
                        
        def solve(idx):
            if idx == m:
                self.ans = max(self.ans, self.score)
                return
            for i in range(m):
                if used_mentors[i] == 1:
                    continue
                used_mentors[i] = 1
                self.score += computed[idx][i]
                solve(idx+1)
                used_mentors[i] = 0
                self.score -= computed[idx][i]
        
        solve(0)
        return self.ans
                

        
        