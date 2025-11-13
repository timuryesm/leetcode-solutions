class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        zero_runs_right = 0   # number of zero blocks in the suffix to the right
        ans = 0

        # Scan from right to left; whenever we pass the last zero of a block,
        # we increase the zero-runs count. Each '1' contributes that count.
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                ans += zero_runs_right
            else:
                if i == n - 1 or s[i + 1] == '1':  # last zero of its block
                    zero_runs_right += 1
        return ans
