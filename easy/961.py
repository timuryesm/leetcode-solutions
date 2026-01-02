class Solution(object):
    def repeatedNTimes(self, nums):
        # Check distances 1..3
        for k in (1, 2, 3):
            for i in range(len(nums) - k):
                if nums[i] == nums[i + k]:
                    return nums[i]
