# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.ans = 0
        def dfs(node):
            freq = [0] * (distance + 1)
            if not node:
                return freq
            if not node.left and not node.right:
                freq[1] = 1
                return freq
            left = dfs(node.left)
            right = dfs(node.right)
            for i in range(distance + 1):
                for j in range(distance + 1):
                    if i + j <= distance:
                        self.ans += left[i] * right[j]
            for i in range(distance):
                freq[i + 1] = left[i] + right[i]
            return freq
        dfs(root)
        return self.ans