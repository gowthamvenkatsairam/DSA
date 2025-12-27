class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = [[] * (n+1) for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis = [0] * (n+1)
        dq = deque([(1, 1, 0)])
        ans = 0.0
        while dq:
            node, prob, time = dq.popleft()
            vis[node] = 1
            unvisited = [nei for nei in graph[node] if vis[nei] == 0]
            if len(unvisited) == 0 or time == t:
                if node == target:
                    return prob
                continue
            curr_prob = (1/len(unvisited)) * prob
            for nei in unvisited:
                dq.append((nei, curr_prob, time + 1))
        return ans
                    


        