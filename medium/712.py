class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n, m = len(s1), len(s2)

        # dp[j] = answer for s1[i:] and s2[j:] while iterating i from n..0
        dp = [0] * (m + 1)

        # base: i = n (s1 empty), must delete rest of s2
        for j in range(m - 1, -1, -1):
            dp[j] = dp[j + 1] + ord(s2[j])

        for i in range(n - 1, -1, -1):
            new = [0] * (m + 1)
            # base: j = m (s2 empty), must delete rest of s1
            new[m] = dp[m] + ord(s1[i])

            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    new[j] = dp[j + 1]
                else:
                    del1 = ord(s1[i]) + dp[j]       # delete s1[i]
                    del2 = ord(s2[j]) + new[j + 1]  # delete s2[j]
                    new[j] = del1 if del1 < del2 else del2

            dp = new

        return dp[0]
