class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = []
        cur = 0  # current value mod 5

        for b in nums:
            cur = (cur * 2 + b) % 5
            res.append(cur == 0)

        return res
