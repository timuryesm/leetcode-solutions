class Solution(object):
    def minimumDifference(self, nums, k):
        if k <= 1:
            return 0
        nums.sort()
        best = float('inf')
        for i in range(len(nums) - k + 1):
            best = min(best, nums[i + k - 1] - nums[i])
        return best
