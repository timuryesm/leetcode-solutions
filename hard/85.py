class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        best = 0

        for r in range(rows):
            # build histogram heights
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # largest rectangle in histogram (heights)
            stack = []  # indices with increasing heights
            for i in range(cols + 1):
                cur_h = heights[i] if i < cols else 0  # sentinel 0 to flush stack
                while stack and cur_h < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    area = h * width
                    if area > best:
                        best = area
                stack.append(i)

        return best
