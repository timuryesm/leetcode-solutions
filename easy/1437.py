class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last = -k - 1  # ensures the first 1 always passes the distance check
        for i, v in enumerate(nums):
            if v == 1:
                if i - last <= k:
                    return False
                last = i
        return True
