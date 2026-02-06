class Solution(object):
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        best = 1
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            best = max(best, j - i)
        return n - best
