class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort by end ascending, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # a = largest chosen point, b = second largest chosen point
        a = b = -1
        ans = 0
        
        for l, r in intervals:
            # Case 1: no chosen points in [l, r]
            if l > a:
                # Add r-1 and r
                ans += 2
                b = r - 1
                a = r
            # Case 2: exactly one chosen point (a) in [l, r]
            elif l > b:
                # Add r
                ans += 1
                b = a
                a = r
            # Case 3: already at least two points inside -> do nothing
        
        return ans
