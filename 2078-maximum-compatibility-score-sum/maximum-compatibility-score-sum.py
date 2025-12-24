class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        self.ans = float("-inf")
        used_mentors = [0] * m
        self.score = 0
        def solve(idx):
            if idx == m:
                self.ans = max(self.ans, self.score)
                return
            for i in range(m):
                same = 0
                if used_mentors[i] == 1: continue
                for k in range(n):
                    if students[idx][k] == mentors[i][k]:
                        same += 1
                used_mentors[i] = 1
                self.score += same
                solve(idx+1)
                used_mentors[i] = 0
                self.score -= same
        solve(0)
        return self.ans
                

        
        