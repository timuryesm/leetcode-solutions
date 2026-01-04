class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for x in nums:
            divs = set([1, x])
            d = 2

            while d * d <= x and len(divs) <= 4:
                if x % d == 0:
                    divs.add(d)
                    divs.add(x // d)
                d += 1

            if len(divs) == 4:
                ans += sum(divs)

        return ans
