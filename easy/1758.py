class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        change1 = 0  # pattern starting with '0'
        change2 = 0  # pattern starting with '1'
        
        for i, c in enumerate(s):
            if c != ('0' if i % 2 == 0 else '1'):
                change1 += 1
            if c != ('1' if i % 2 == 0 else '0'):
                change2 += 1
        
        return min(change1, change2)
