class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}
        def f(idx, prev_idx_swapped):
            if idx == len(nums1):
                return 0
            if idx == 0:
                return min(f(1, 0), 1 + f(1, 1))
            if (idx, prev_idx_swapped) in dp:
                return dp[(idx, prev_idx_swapped)]
            prev1, prev2 = nums1[idx - 1], nums2[idx - 1]
            if prev_idx_swapped:
                prev1, prev2 = prev2 , prev1
            swap, not_swap = float("inf"), float("inf")
            if nums1[idx] > prev1 and nums2[idx] > prev2:
                not_swap = f(idx + 1, 0)
            if nums1[idx] > prev2 and nums2[idx] > prev1:
                swap = 1 + f(idx + 1, 1)
            dp[(idx, prev_idx_swapped)] = min(swap, not_swap)
            return dp[(idx, prev_idx_swapped)] 
        return f(0, 0)

