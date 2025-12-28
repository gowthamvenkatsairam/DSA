class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = 0, n - 1
        cnt = 0
        while 0 <= i < m and 0 <= j < n:
            if grid[i][j] < 0:
                cnt += m - i
                j -= 1
            else: i += 1
        return cnt

        