class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        heap = []
        result = []
        for string in words:
            freq[string] = freq.get(string, 0) + 1
        for string, cnt in freq.items():
            heapq.heappush(heap, (-cnt, string))
        while heap and len(result) < k:
            cnt, string = heapq.heappop(heap)
            result.append(string)
        return result




        