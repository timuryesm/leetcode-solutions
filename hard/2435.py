class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        # dp[i][j][r] = #paths to (i,j) with sum % k == r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        first_val = grid[0][0] % k
        dp[0][0][first_val] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j] % k
                for r in range(k):
                    if i > 0 and dp[i-1][j][r]:
                        dp[i][j][(r + val) % k] = (dp[i][j][(r + val) % k] + dp[i-1][j][r]) % MOD
                    if j > 0 and dp[i][j-1][r]:
                        dp[i][j][(r + val) % k] = (dp[i][j][(r + val) % k] + dp[i][j-1][r]) % MOD
        
        return dp[m-1][n-1][0]
