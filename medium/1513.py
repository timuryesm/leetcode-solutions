class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        run = 0

        for ch in s:
            if ch == '1':
                run += 1
            else:
                if run:
                    ans = (ans + run * (run + 1) // 2) % MOD
                    run = 0

        # Add the last run if string ends with '1'
        if run:
            ans = (ans + run * (run + 1) // 2) % MOD

        return ans
