class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Precompute all perfect squares c^2 with 1 <= c <= n
        squares = {c * c for c in range(1, n + 1)}
        
        count = 0
        # Check all pairs (a, b)
        for a in range(1, n + 1):
            a2 = a * a
            for b in range(1, n + 1):
                if a2 + b * b in squares:
                    count += 1
        
        return count
