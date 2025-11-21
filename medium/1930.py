class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        # first[i] = first index of chr(i + ord('a')) in s
        # last[i]  = last index of chr(i + ord('a')) in s
        first = [n] * 26
        last = [-1] * 26
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if i < first[idx]:
                first[idx] = i
            if i > last[idx]:
                last[idx] = i
        
        ans = 0
        
        # For each letter as the outer character of the palindrome
        for c in range(26):
            if first[c] < last[c]:  # appears at least twice
                l = first[c]
                r = last[c]
                # distinct middle characters between l and r
                middle_chars = set(s[l+1:r])
                ans += len(middle_chars)
        
        return ans
