class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        r, c = 0, n - 1
        ans = 0

        while r < m and c >= 0:
            if grid[r][c] < 0:
                ans += (m - r)
                c -= 1
            else:
                r += 1

        return ans
