class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def getSubsets(path, start):
            result.append(path[:])
            if len(path) == n:
                return
            for i in range(start, n):
                path.append(nums[i])
                getSubsets(path, i + 1)
                path.pop()
        getSubsets([], 0)
        return result

        