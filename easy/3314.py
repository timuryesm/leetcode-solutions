class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for p in nums:
            # If p is even, it's impossible (only even prime is 2, but rule holds generally)
            if (p & 1) == 0:
                ans.append(-1)
                continue

            # Count trailing ones in p
            k = 0
            temp = p
            while (temp & 1) == 1:
                k += 1
                temp >>= 1

            # Minimal x is p with the highest bit in the trailing-ones block cleared
            ans.append(p - (1 << (k - 1)))

        return ans
