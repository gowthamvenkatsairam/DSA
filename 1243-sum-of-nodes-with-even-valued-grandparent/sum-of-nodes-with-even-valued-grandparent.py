# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(node, par, g_par):
            if not node:
                return
            if g_par and g_par % 2 == 0:
                self.result += node.val
            dfs(node.left, node.val, par)
            dfs(node.right, node.val, par)
        dfs(root, None, None) 
        return self.result           
            

        