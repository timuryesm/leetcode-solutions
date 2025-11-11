class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        0/1 knapsack on two resources: zeros (m) and ones (n).
        dp[i][j] = max strings using at most i zeros and j ones.
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Precompute counts of 0s and 1s for each string
        counts = []
        for s in strs:
            z = s.count('0')
            o = len(s) - z
            counts.append((z, o))

        # For each string, update dp backwards (0/1 knapsack)
        for z, o in counts:
            for i in range(m, z - 1, -1):
                for j in range(n, o - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - z][j - o] + 1)

        return dp[m][n]
