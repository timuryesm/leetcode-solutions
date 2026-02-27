class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0
        o = n - z

        # If we must flip all indices every time, we can only toggle s <-> ~s
        if k == n:
            return 1 if z == n else -1

        start = (z + k - 1) // k  # need at least z flips total
        for m in range(start, n + 1):
            S = m * k
            if (S & 1) != (z & 1):
                continue

            maxSum = n * m - (z if m % 2 == 0 else o)
            if z <= S <= maxSum:
                return m

        return -1
