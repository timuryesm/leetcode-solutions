class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        Kmax = min(m, n)

        # row prefix sums: rowP[i][j+1] = sum(grid[i][0..j])
        rowP = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            s = 0
            for j in range(n):
                s += grid[i][j]
                rowP[i][j + 1] = s

        # col prefix sums: colP[i+1][j] = sum(grid[0..i][j])
        colP = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            s = 0
            for i in range(m):
                s += grid[i][j]
                colP[i + 1][j] = s

        # main diagonal prefix (down-right): d1[i+1][j+1] = grid[i][j] + d1[i][j]
        d1 = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                d1[i + 1][j + 1] = grid[i][j] + d1[i][j]

        # anti-diagonal prefix (down-left):
        # d2[i+1][j] = grid[i][j] + d2[i][j+1]
        d2 = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                d2[i + 1][j] = grid[i][j] + d2[i][j + 1]

        def row_sum(r, c, k):
            return rowP[r][c + k] - rowP[r][c]

        def col_sum(r, c, k):
            return colP[r + k][c] - colP[r][c]

        def diag_sum(r, c, k):
            # from (r,c) to (r+k-1,c+k-1)
            return d1[r + k][c + k] - d1[r][c]

        def anti_diag_sum(r, c, k):
            # from (r,c+k-1) to (r+k-1,c)
            return d2[r + k][c] - d2[r][c + k]

        # Try larger squares first
        for k in range(Kmax, 1, -1):
            for r in range(0, m - k + 1):
                for c in range(0, n - k + 1):
                    target = row_sum(r, c, k)

                    # diagonals must match
                    if diag_sum(r, c, k) != target:
                        continue
                    if anti_diag_sum(r, c, k) != target:
                        continue

                    ok = True
                    # check all rows
                    for i in range(r, r + k):
                        if row_sum(i, c, k) != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    # check all cols
                    for j in range(c, c + k):
                        if col_sum(r, j, k) != target:
                            ok = False
                            break

                    if ok:
                        return k

        return 1
