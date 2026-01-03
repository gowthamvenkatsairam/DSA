class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dq.append((i, j, 0))
        while dq:
            i, j, distance = dq.popleft()
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == 2147483647:
                    rooms[ni][nj] = distance + 1
                    dq.append((ni, nj, distance + 1))






        
