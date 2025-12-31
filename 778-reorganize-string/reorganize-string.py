class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freq = {}
        n = len(s)
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch, cnt in freq.items():
            heapq.heappush(heap, (-cnt, ch))
        res = []
        prev = None
        while heap:
            cnt, ch = heapq.heappop(heap)
            res.append(ch)
            if prev != None:
                heapq.heappush(heap, prev)
            prev = (cnt+1, ch) if cnt != -1 else None
        return "" if len(res) != n else "".join(res)

        


            
