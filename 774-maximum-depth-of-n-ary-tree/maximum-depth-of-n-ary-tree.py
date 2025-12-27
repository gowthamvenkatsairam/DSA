"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0
        def dfs(node, depth):
            if not node:
                return 0
            depth += 1
            if len(node.children) == 0:
                self.max_depth = max(self.max_depth, depth)
            for child in node.children:
                dfs(child, depth)
        dfs(root, 0)
        return self.max_depth
