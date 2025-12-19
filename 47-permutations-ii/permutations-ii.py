class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        used = [0] * n
        result = []
        def f(arr):
            if len(arr) == n:
                result.append(arr[:])
                return
            for i in range(n):
                if used[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                arr.append(nums[i])
                used[i] = 1
                f(arr)
                used[i] = 0
                arr.pop()
        f([])
        return result

            
        
        
        