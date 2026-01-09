class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return (0, None)  # depth, answer node

            ld, lnode = dfs(node.left)
            rd, rnode = dfs(node.right)

            if ld > rd:
                return (ld + 1, lnode)
            elif rd > ld:
                return (rd + 1, rnode)
            else:
                return (ld + 1, node)

        return dfs(root)[1]
