# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([root])
        depth = -1
        while dq:
            lvl = []
            depth += 1
            lvl_size = len(dq)
            for _ in range(lvl_size):
                node = dq.popleft()
                lvl.append(node)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            if depth % 2 == 1:
                l, r = 0, len(lvl) - 1
                while l < r:
                    lvl[l].val, lvl[r].val = lvl[r].val, lvl[l].val
                    l += 1
                    r -= 1
        return root



        