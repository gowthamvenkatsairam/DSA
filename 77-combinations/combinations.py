class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def getCombination(path, start):
            if len(path) == k:
                result.append(path[:])
                return 
            for num in range(start, n+1):
                path.append(num)
                getCombination(path, num+1)
                path.pop()
        getCombination([], 1)
        return result
 


        