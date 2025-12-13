class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        
        def valid_code(s):
            if not s:
                return False
            for ch in s:
                if not (ch.isalnum() or ch == "_"):
                    return False
            return True
        
        valid = []
        for c, bl, active in zip(code, businessLine, isActive):
            if not active:
                continue
            if bl not in order:
                continue
            if not valid_code(c):
                continue
            valid.append((order[bl], c))
        
        valid.sort(key=lambda x: (x[0], x[1]))
        return [c for _, c in valid]
