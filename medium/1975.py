class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        neg = 0
        mn = 10**18

        for row in matrix:
            for x in row:
                if x < 0:
                    neg += 1
                ax = -x if x < 0 else x
                total += ax
                if ax < mn:
                    mn = ax

        if neg % 2 == 0:
            return total
        return total - 2 * mn
