from collections import Counter

class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        def removable_from_top(diff, top_counter, top_rows):
            cells = top_rows * n
            if cells <= 1:
                return False

            if top_rows >= 2 and n >= 2:
                return diff in top_counter

            # one row
            if top_rows == 1:
                return grid[0][0] == diff or grid[0][n - 1] == diff

            # one column
            return grid[0][0] == diff or grid[top_rows - 1][0] == diff

        def removable_from_bottom(diff, bottom_counter, top_rows):
            bottom_rows = m - top_rows
            cells = bottom_rows * n
            if cells <= 1:
                return False

            if bottom_rows >= 2 and n >= 2:
                return diff in bottom_counter

            # one row
            if bottom_rows == 1:
                r = m - 1
                return grid[r][0] == diff or grid[r][n - 1] == diff

            # one column
            return grid[top_rows][0] == diff or grid[m - 1][0] == diff

        def removable_from_left(diff, left_counter, left_cols):
            cells = m * left_cols
            if cells <= 1:
                return False

            if m >= 2 and left_cols >= 2:
                return diff in left_counter

            # one column
            if left_cols == 1:
                return grid[0][0] == diff or grid[m - 1][0] == diff

            # one row
            return grid[0][0] == diff or grid[0][left_cols - 1] == diff

        def removable_from_right(diff, right_counter, left_cols):
            right_cols = n - left_cols
            cells = m * right_cols
            if cells <= 1:
                return False

            if m >= 2 and right_cols >= 2:
                return diff in right_counter

            # one column
            if right_cols == 1:
                c = n - 1
                return grid[0][c] == diff or grid[m - 1][c] == diff

            # one row
            return grid[0][left_cols] == diff or grid[0][n - 1] == diff

        # Try horizontal cuts
        top_counter = Counter()
        bottom_counter = Counter()
        for row in grid:
            bottom_counter.update(row)

        top_sum = 0
        for r in range(m - 1):
            for val in grid[r]:
                top_sum += val
                top_counter[val] += 1
                bottom_counter[val] -= 1
                if bottom_counter[val] == 0:
                    del bottom_counter[val]

            bottom_sum = total - top_sum
            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)
            if top_sum > bottom_sum:
                if removable_from_top(diff, top_counter, r + 1):
                    return True
            else:
                if removable_from_bottom(diff, bottom_counter, r + 1):
                    return True

        # Try vertical cuts
        left_counter = Counter()
        right_counter = Counter()
        for i in range(m):
            for j in range(n):
                right_counter[grid[i][j]] += 1

        left_sum = 0
        for c in range(n - 1):
            for i in range(m):
                val = grid[i][c]
                left_sum += val
                left_counter[val] += 1
                right_counter[val] -= 1
                if right_counter[val] == 0:
                    del right_counter[val]

            right_sum = total - left_sum
            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)
            if left_sum > right_sum:
                if removable_from_left(diff, left_counter, c + 1):
                    return True
            else:
                if removable_from_right(diff, right_counter, c + 1):
                    return True

        return False
