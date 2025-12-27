"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return root
        dq = deque([root])
        result = []
        while dq:
            level = []
            for _ in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                for node in node.children:
                    dq.append(node)
            result.append(level)
        return result

                
        