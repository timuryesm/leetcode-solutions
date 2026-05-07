class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # suffix minimums
        suf_min = [0] * n
        suf_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suf_min[i] = min(nums[i], suf_min[i + 1])

        ans = [0] * n

        start = 0
        cur_max = nums[0]

        for i in range(n - 1):
            cur_max = max(cur_max, nums[i])

            # split point:
            # everything on left <= everything on right
            if cur_max <= suf_min[i + 1]:
                comp_max = max(nums[start:i + 1])

                for j in range(start, i + 1):
                    ans[j] = comp_max

                start = i + 1
                cur_max = nums[start]

        # last component
        comp_max = max(nums[start:])

        for j in range(start, n):
            ans[j] = comp_max

        return ans
