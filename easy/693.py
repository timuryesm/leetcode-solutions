class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n & 1
        n >>= 1
        
        while n:
            curr = n & 1
            if curr == prev:
                return False
            prev = curr
            n >>= 1
        
        return True
