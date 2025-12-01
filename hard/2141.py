class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        total = sum(batteries)
        
        # Upper bound: even with perfect splitting we can't exceed total // n
        left, right = 0, total // n
        
        def can_run(t):
            # Check if we can run n computers for t minutes
            # Each battery contributes at most min(b, t)
            need = n * t
            acc = 0
            for b in batteries:
                acc += b if b < t else t
                if acc >= need:
                    return True
            return acc >= need
        
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can_run(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
