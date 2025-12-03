from collections import defaultdict

class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        # cnt1: slope k -> (intercept b -> number of segments with that (k,b))
        cnt1 = defaultdict(lambda: defaultdict(int))
        # cnt2: encoded midpoint p -> (slope k -> number of segments with that midpoint and slope)
        cnt2 = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    # vertical line: use big number for slope and x as "intercept"
                    k = 1e9
                    b = x1
                else:
                    k = float(dy) / dx
                    b = float(y1 * dx - x1 * dy) / dx

                # Normalize -0.0 to 0.0 to avoid duplicate float keys
                if k == -0.0:
                    k = 0.0
                if b == -0.0:
                    b = 0.0

                # Count segments per line (k, b)
                cnt1[k][b] += 1

                # Encode midpoint (x1 + x2, y1 + y2) into a single integer key
                # Coordinates are in [-1000, 1000], so sums are in [-2000, 2000]
                p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
                cnt2[p][k] += 1

        ans = 0

        # Step 1: For each slope k, count pairs of segments on different parallel lines
        # For fixed k: lines have intercepts b1, b2, ... with counts t1, t2, ...
        # Number of pairs of segments on different lines: sum_{i<j} t_i * t_j
        for lines in cnt1.values():
            s = 0
            for t in lines.values():
                ans += s * t
                s += t

        # Step 2: Subtract over-counted cases using midpoint grouping.
        # For each midpoint p: segments grouped by slope.
        # Overlaps from parallelogram-like configurations are subtracted.
        for slopes in cnt2.values():
            s = 0
            for t in slopes.values():
                ans -= s * t
                s += t

        return ans
