class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        length = 0
        
        for i in range(1, n + 1):
            # if i is power of 2, increase bit length
            if (i & (i - 1)) == 0:
                length += 1
            
            ans = ((ans << length) | i) % MOD
        
        return ans
