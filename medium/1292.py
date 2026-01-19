class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        # Build prefix sum ps where ps[i+1][j+1] = sum of mat[0..i][0..j]
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row_sum

        def square_sum(r, c, size):
            r2, c2 = r + size, c + size
            return ps[r2][c2] - ps[r][c2] - ps[r2][c] + ps[r][c]

        def exists(size):
            if size == 0:
                return True
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if square_sum(i, j, size) <= threshold:
                        return True
            return False

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if exists(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
