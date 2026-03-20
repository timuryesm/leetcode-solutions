class Solution(object):
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                values = set()
                
                # collect distinct values in k x k submatrix
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        values.add(grid[r][c])
                
                values = sorted(values)
                
                if len(values) < 2:
                    ans[i][j] = 0
                    continue
                
                best = float('inf')
                for t in range(1, len(values)):
                    best = min(best, values[t] - values[t - 1])
                
                ans[i][j] = best
        
        return ans
