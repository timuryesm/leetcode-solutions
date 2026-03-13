import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        
        def can_finish(time):
            total = 0
            
            for w in workerTimes:
                k = (2 * time) // w
                x = int((math.sqrt(1 + 4 * k) - 1) // 2)
                total += x
                
                if total >= mountainHeight:
                    return True
            
            return False
        
        left = 0
        right = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        
        while left < right:
            mid = (left + right) // 2
            
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
