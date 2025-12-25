# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return None, depth
            depth += 1
            if node.left == None and node.right == None:
                return node, depth
            left_lca, left_depth = dfs(node.left, depth)
            right_lca, right_depth = dfs(node.right, depth)
            if left_depth > right_depth:
                return left_lca, left_depth
            elif right_depth > left_depth:
                return right_lca, right_depth
            else: return node, left_depth
        lca, depth = dfs(root, 1)
        return lca
        