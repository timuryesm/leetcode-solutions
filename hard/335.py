class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        d = distance
        n = len(d)
        
        # A path with fewer than 4 lines cannot cross itself
        if n < 4:
            return False
            
        for i in range(3, n):
            # Case 1: Current line crosses the line from 3 steps ago
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True
                
            # Case 2: Current line matches up and intersects with line from 4 steps ago
            if i >= 4 and d[i-1] == d[i-3] and d[i] + d[i-4] >= d[i-2]:
                return True
                
            # Case 3: Current line crosses the line from 5 steps ago (spiral contraction)
            if i >= 5 and d[i-1] <= d[i-3] and d[i-2] > d[i-4] and \
               d[i-1] + d[i-5] >= d[i-3] and d[i] + d[i-4] >= d[i-2]:
                return True
                
        return False
