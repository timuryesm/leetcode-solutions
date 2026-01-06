# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque([root])
        level = 1
        best_level = 1
        best_sum = -10**18

        while q:
            size = len(q)
            s = 0
            for _ in range(size):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if s > best_sum:
                best_sum = s
                best_level = level

            level += 1

        return best_level
