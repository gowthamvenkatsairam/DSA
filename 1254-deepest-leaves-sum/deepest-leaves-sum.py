# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_depth, self.result = 0, 0
        def dfs(node, depth):
            if not node:
                return 
            depth += 1
            if not node.left and not node.right:
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.result = node.val
                elif depth == self.max_depth:
                    self.result += node.val
                else: return
            dfs(node.left, depth)
            dfs(node.right, depth)
        dfs(root, 0)
        return self.result

        