class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis = [0] * n
        ans = [0] * n
        def dfs(node):
            vis[node] = 1
            freq = [0] * 26
            for child in graph[node]:
                if vis[child] != 1:
                    subtree_freq = dfs(child)
                    for i in range(26):
                        freq[i] += subtree_freq[i]
            freq[ord(labels[node]) - ord("a")] += 1
            ans[node] = freq[ord(labels[node]) - ord("a")]
            return freq
        dfs(0)
        return ans
        
