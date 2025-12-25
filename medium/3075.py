class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            val = happiness[i] - i
            if val <= 0:
                break
            ans += val
        return ans
