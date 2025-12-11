class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        INF = 10**18
        
        # Using size n+1 because coordinates are 1-based
        row_min = [INF] * (n + 1)
        row_max = [-INF] * (n + 1)
        col_min = [INF] * (n + 1)
        col_max = [-INF] * (n + 1)
        
        # First pass: compute min/max per row and column
        for x, y in buildings:
            if y < row_min[x]:
                row_min[x] = y
            if y > row_max[x]:
                row_max[x] = y
            if x < col_min[y]:
                col_min[y] = x
            if x > col_max[y]:
                col_max[y] = x
        
        # Second pass: count covered buildings
        ans = 0
        for x, y in buildings:
            if (y > row_min[x] and y < row_max[x] and
                x > col_min[y] and x < col_max[y]):
                ans += 1
        
        return ans
