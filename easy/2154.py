class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums_set = set(nums)

        while original in nums_set:
            original *= 2

        return original
