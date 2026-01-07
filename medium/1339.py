class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        MOD = 10**9 + 7

        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        T = total_sum(root)
        best = [0]  # mutable container for Python 2

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            prod = s * (T - s)
            if prod > best[0]:
                best[0] = prod
            return s

        dfs(root)
        return best[0] % MOD
