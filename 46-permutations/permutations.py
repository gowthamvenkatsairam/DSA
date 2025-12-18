class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        used = [0] * n
        def f(arr, used):
            if len(arr) == n:
                result.append(arr[:])
            for i in range(n):
                if used[i] == 0:
                    arr.append(nums[i])
                    used[i] = 1
                    f(arr, used)
                    arr.pop()
                    used[i] = 0
        f([], used)
        return result
                
                
                
            

        