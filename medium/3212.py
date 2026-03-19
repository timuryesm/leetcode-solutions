class Solution(object):
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Convert grid to values
        val = [[0]*n for _ in range(m)]
        xcnt = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    val[i][j] = 1
                    xcnt[i][j] = 1
                elif grid[i][j] == 'Y':
                    val[i][j] = -1
        
        res = 0
        
        # Build prefix sums
        for i in range(m):
            for j in range(n):
                if i > 0:
                    val[i][j] += val[i-1][j]
                    xcnt[i][j] += xcnt[i-1][j]
                if j > 0:
                    val[i][j] += val[i][j-1]
                    xcnt[i][j] += xcnt[i][j-1]
                if i > 0 and j > 0:
                    val[i][j] -= val[i-1][j-1]
                    xcnt[i][j] -= xcnt[i-1][j-1]
                
                # Check conditions
                if val[i][j] == 0 and xcnt[i][j] > 0:
                    res += 1
        
        return res
