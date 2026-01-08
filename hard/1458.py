class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        NEG = -10**18

        # dp[j] represents dp for current i at column j (1..m)
        dp = [NEG] * (m + 1)

        for i in range(1, n + 1):
            prev_diag = NEG  # this will hold dp[i-1][j-1]
            new_dp0 = NEG    # dp[i][0] stays NEG (can't form non-empty with empty second array)
            # We'll update dp in-place; keep old dp[j] as dp[i-1][j]
            for j in range(1, m + 1):
                old_dp_j = dp[j]  # dp[i-1][j] before overwrite

                prod = nums1[i - 1] * nums2[j - 1]
                take = prod + (0 if prev_diag < 0 else prev_diag)  # prod + max(0, dp[i-1][j-1])

                # dp[i][j] = max(dp[i-1][j], dp[i][j-1], take)
                best = old_dp_j
                if dp[j - 1] > best:   # dp[j-1] is already updated => dp[i][j-1]
                    best = dp[j - 1]
                if take > best:
                    best = take

                prev_diag = old_dp_j
                dp[j] = best

        return dp[m]
