class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # minPref[r] = minimum prefix sum seen at indices with index % k == r
        INF = float('inf')
        minPref = [INF] * k
        
        # prefix sum at index 0 is 0, with index 0 % k == 0
        prefix = 0
        minPref[0] = 0
        
        ans = -10**30  # sufficiently small
        
        for i, x in enumerate(nums, 1):  # i is prefix index (1..n)
            prefix += x
            r = i % k
            
            if minPref[r] != INF:
                ans = max(ans, prefix - minPref[r])
            
            if prefix < minPref[r]:
                minPref[r] = prefix
        
        return ans
