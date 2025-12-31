class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set()
        factors = [2, 3, 5]
        for _ in range(n):
            num = heapq.heappop(heap)
            while heap and num in seen:
                num = heapq.heappop(heap)
            seen.add(num)
            for factor in factors:
                heapq.heappush(heap, num * factor)
        return num


            




        