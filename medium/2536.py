class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        # 2D difference array (size n+1 x n+1 to handle edges easily)
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Prefix sum across rows
        for i in range(n):
            run = 0
            for j in range(n):
                run += diff[i][j]
                diff[i][j] = run

        # Prefix sum down columns
        for j in range(n):
            run = 0
            for i in range(n):
                run += diff[i][j]
                diff[i][j] = run

        # Extract the n x n result
        return [row[:n] for row in diff[:n]]
