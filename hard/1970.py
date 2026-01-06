from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        def can_cross(day):
            # grid[r][c] = 1 water, 0 land
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            q = deque()
            seen = [[False] * col for _ in range(row)]

            # start from all land cells in top row
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    seen[0][c] = True

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and not seen[nr][nc] and grid[nr][nc] == 0:
                        seen[nr][nc] = True
                        q.append((nr, nc))
            return False

        lo, hi = 0, row * col  # day in [0..R*C]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_cross(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
