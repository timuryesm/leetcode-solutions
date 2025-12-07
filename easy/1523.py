class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # If either low or high is odd, the interval contains one extra odd number
        if low % 2 == 1 or high % 2 == 1:
            return (high - low) // 2 + 1
        else:
            return (high - low) // 2
