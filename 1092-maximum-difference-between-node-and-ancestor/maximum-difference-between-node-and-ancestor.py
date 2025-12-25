# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(node, curr_min, curr_max):
            if not node:
                return
            self.result = max(self.result, abs(node.val-curr_min), abs(node.val-curr_max))
            curr_max, curr_min = max(curr_max, node.val), min(curr_min, node.val) 
            dfs(node.left, curr_min, curr_max)
            dfs(node.right, curr_min, curr_max)
        dfs(root, root.val, root.val)
        return self.result
            
        