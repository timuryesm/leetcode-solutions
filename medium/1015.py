class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        # If k has factor 2 or 5, no repunit (all 1s) can be divisible by k
        if k % 2 == 0 or k % 5 == 0:
            return -1

        rem = 0
        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length

        # If we didn't find a remainder 0 in k steps, it's impossible
        return -1
