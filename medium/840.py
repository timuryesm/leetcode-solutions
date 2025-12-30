class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        if R < 3 or C < 3:
            return 0

        def is_magic(r, c):
            # center must be 5
            if grid[r+1][c+1] != 5:
                return False

            seen = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    v = grid[i][j]
                    if v < 1 or v > 9 or v in seen:
                        return False
                    seen.add(v)

            s = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            # rows
            if grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != s:
                return False
            if grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != s:
                return False
            # cols
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != s:
                return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != s:
                return False
            # diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False

            return True

        ans = 0
        for r in range(R - 2):
            for c in range(C - 2):
                if is_magic(r, c):
                    ans += 1
        return ans
