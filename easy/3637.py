class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # strictly increasing (need at least 2 elements)
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False  # no first increase or ended too early

        # strictly decreasing (need at least 2 elements)
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == n - 1:
            return False  # no final increasing part

        # strictly increasing to the end (need at least 2 elements)
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
