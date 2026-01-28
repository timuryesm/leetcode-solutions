class Solution(object):
    def minCost(self, grid, k):
        n, m = len(grid), len(grid[0])

        maxVal = 0
        for row in grid:
            for v in row:
                if v > maxVal:
                    maxVal = v

        INF = 10**18
        dp = [[INF] * m for _ in range(n)]
        temp = [INF] * (maxVal + 1)
        best = [INF] * (maxVal + 1)

        # base: target -> target costs 0 additional
        dp[n - 1][m - 1] = 0
        temp[grid[n - 1][m - 1]] = 0

        # k = 0 walking DP
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    continue
                down = dp[i + 1][j] + grid[i + 1][j] if i + 1 < n else INF
                right = dp[i][j + 1] + grid[i][j + 1] if j + 1 < m else INF
                dp[i][j] = down if down < right else right
                v = grid[i][j]
                if dp[i][j] < temp[v]:
                    temp[v] = dp[i][j]

        # layers for teleports
        for _ in range(k):
            # prefix mins over values
            best[0] = temp[0]
            for v in range(1, maxVal + 1):
                prev = best[v - 1]
                cur = temp[v]
                best[v] = cur if cur < prev else prev

            # relax dp with teleport option
            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    if i == n - 1 and j == m - 1:
                        continue
                    down = dp[i + 1][j] + grid[i + 1][j] if i + 1 < n else INF
                    right = dp[i][j + 1] + grid[i][j + 1] if j + 1 < m else INF
                    walkCost = down if down < right else right
                    teleCost = best[grid[i][j]]
                    dp[i][j] = teleCost if teleCost < walkCost else walkCost

                    v = grid[i][j]
                    if dp[i][j] < temp[v]:
                        temp[v] = dp[i][j]

        return dp[0][0]
