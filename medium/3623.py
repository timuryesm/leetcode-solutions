from collections import Counter

class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        inv2 = (MOD + 1) // 2  # modular inverse of 2 under MOD
        
        # Count how many points share the same y-coordinate
        y_count = Counter()
        for x, y in points:
            y_count[y] += 1
        
        # For each horizontal line, compute number of ways to pick 2 points on it
        # a_i = C(cnt, 2)
        S = 0   # sum of a_i
        S2 = 0  # sum of a_i^2
        for cnt in y_count.values():
            if cnt >= 2:
                a = cnt * (cnt - 1) // 2
                a %= MOD
                S = (S + a) % MOD
                S2 = (S2 + a * a) % MOD
        
        # If fewer than two y-levels have at least 2 points, no trapezoids
        if S == 0:
            return 0
        
        # Number of trapezoids: (S^2 - S2) / 2  (mod MOD)
        ans = (S * S - S2) % MOD
        ans = (ans * inv2) % MOD
        return ans
