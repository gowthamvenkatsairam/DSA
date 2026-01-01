class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        heap = []
        dq = deque()
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch, cnt in freq.items():
            heapq.heappush(heap, (-cnt, ch))
        result = [0] * len(s)
        for i in range(len(s)):
            while dq and i >= dq[0][0]:
                a, b, ch = dq.popleft()
                heapq.heappush(heap, (b, ch))
            if not heap:
                return ""
            cnt, ch = heapq.heappop(heap)
            result[i] = ch
            if cnt != -1:
                next_avl = i + k
                dq.append((next_avl, cnt + 1, ch))
        return "".join(result)





        