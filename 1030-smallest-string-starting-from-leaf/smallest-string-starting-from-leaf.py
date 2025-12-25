# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.min_str = None
        path = []
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                path.append(chr(ord("a") + node.val))
                curr_str = "".join(path[::-1])
                if self.min_str is None or curr_str < self.min_str:
                    self.min_str = curr_str
                path.pop()
                return
            path.append(chr(ord("a") + node.val))
            dfs(node.left)
            dfs(node.right)
            path.pop()
        dfs(root)
        return self.min_str
            


        