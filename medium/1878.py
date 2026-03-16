class Solution(object):
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        res = set()
        
        for i in range(m):
            for j in range(n):
                res.add(grid[i][j])
                
                k = 1
                while i-k >= 0 and i+k < m and j-k >= 0 and j+k < n:
                    s = 0
                    
                    for d in range(k):
                        s += grid[i-k+d][j+d]
                    for d in range(k):
                        s += grid[i+d][j+k-d]
                    for d in range(k):
                        s += grid[i+k-d][j-d]
                    for d in range(k):
                        s += grid[i-d][j-k+d]
                    
                    res.add(s)
                    k += 1
        
        return sorted(res, reverse=True)[:3]
