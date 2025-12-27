# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dq = deque([root])
        result = []
        while dq:
            total, cnt = 0, 0
            for _ in range(len(dq)):
                node = dq.popleft()
                total += node.val
                cnt += 1
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            result.append(total/cnt)
        return result

        