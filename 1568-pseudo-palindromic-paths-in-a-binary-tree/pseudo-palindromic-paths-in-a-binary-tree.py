# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        def dfs(node, freq):
            if not node:
                return
            if not node.left and not node.right:
                if bin(freq ^ (1 << node.val)).count("1") <= 1:
                    self.cnt += 1
            dfs(node.left, freq ^ (1 << node.val))
            dfs(node.right, freq ^ (1 << node.val))
        dfs(root, 0)
        return self.cnt



        