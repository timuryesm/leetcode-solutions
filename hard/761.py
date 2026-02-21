class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 2:
            return s
        
        count = 0
        start = 0
        parts = []
        
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1
            
            # Found a balanced special substring
            if count == 0:
                # Recursively process inside
                inner = self.makeLargestSpecial(s[start + 1:i])
                parts.append("1" + inner + "0")
                start = i + 1
        
        # Sort in descending lexicographical order
        parts.sort(reverse=True)
        
        return "".join(parts)
