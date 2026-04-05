import bisect

class Solution:
    def maxWalls(self, robots, distance, walls):
        n = len(robots)

        left = [0] * n
        right = [0] * n
        num = [0] * n

        robots_to_distance = {robots[i]: distance[i] for i in range(n)}

        robots.sort()
        walls.sort()

        for i in range(n):
            r = robots[i]
            d = robots_to_distance[r]

            pos1 = bisect.bisect_right(walls, r)

            if i > 0:
                left_bound = max(r - d, robots[i - 1] + 1)
            else:
                left_bound = r - d

            left_pos = bisect.bisect_left(walls, left_bound)
            left[i] = pos1 - left_pos

            if i < n - 1:
                right_bound = min(r + d, robots[i + 1] - 1)
            else:
                right_bound = r + d

            right_pos = bisect.bisect_right(walls, right_bound)

            pos2 = bisect.bisect_left(walls, r)
            right[i] = right_pos - pos2

            if i > 0:
                pos3 = bisect.bisect_left(walls, robots[i - 1])
                num[i] = pos1 - pos3

        sub_left = left[0]
        sub_right = right[0]

        for i in range(1, n):
            current_left = max(
                sub_left + left[i],
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i])
            )

            current_right = max(
                sub_left + right[i],
                sub_right + right[i]
            )

            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)
