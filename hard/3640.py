class Solution(object):
    def maxSumTrionic(self, nums):
        NEG = -10**30
        n = len(nums)

        dp0 = NEG  # inc (>=2 nodes), ends at i
        dp1 = NEG  # inc then dec (dec has >=2 nodes), ends at i
        dp2 = NEG  # inc then dec then inc (last inc has >=2 nodes), ends at i
        ans = NEG

        for i in range(1, n):
            a, b = nums[i - 1], nums[i]

            new0 = new1 = new2 = NEG

            if b > a:  # increasing edge
                new0 = max(a + b, dp0 + b)
                new2 = max(dp1 + b, dp2 + b)
            elif b < a:  # decreasing edge
                new1 = max(dp0 + b, dp1 + b)
            # if equal: all reset to NEG

            dp0, dp1, dp2 = new0, new1, new2
            if dp2 > ans:
                ans = dp2

        return ans
