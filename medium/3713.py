class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 1  # at least 1 char is always balanced
        
        for i in range(n):
            freq = [0] * 26
            max_freq = 0
            distinct = 0
            
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                
                if freq[idx] == 0:
                    distinct += 1
                
                freq[idx] += 1
                max_freq = max(max_freq, freq[idx])
                
                length = j - i + 1
                
                if length == max_freq * distinct:
                    ans = max(ans, length)
        
        return ans
