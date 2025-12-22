class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])
        
        dp = [1] * m  # LIS length ending at column j
        
        for j in range(m):
            for i in range(j):
                # Check if column i can come before column j in ALL rows
                ok = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        ok = False
                        break
                if ok:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        keep = max(dp)
        return m - keep
