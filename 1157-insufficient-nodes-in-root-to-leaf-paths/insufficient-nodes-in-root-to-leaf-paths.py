# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, total):
            if not node:
                return False
            total += node.val
            if not node.left and not node.right:
                return total >= limit
            left_possible = dfs(node.left, total)
            right_possible = dfs(node.right, total)
            if left_possible == False:
                node.left = None
            if right_possible == False:
                node.right = None
            return left_possible or right_possible
        return root if dfs(root, 0) != False else None



        