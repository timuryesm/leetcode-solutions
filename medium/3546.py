class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        # If total sum is odd → impossible
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # --- Check horizontal cuts ---
        prefix = 0
        for i in range(m - 1):  # must leave at least one row below
            prefix += sum(grid[i])
            if prefix == target:
                return True
        
        # --- Check vertical cuts ---
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
        
        prefix = 0
        for j in range(n - 1):  # must leave at least one column right
            prefix += col_sums[j]
            if prefix == target:
                return True
        
        return False
