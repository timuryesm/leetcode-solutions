class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        memo = {}
        
        def dp(i, j):
            if i == n:
                return 0
            if j == m:
                return float('inf')
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            # خيار: skip this factory
            res = dp(i, j + 1)
            
            pos, limit = factory[j]
            cost = 0
            
            # assign k robots
            for k in range(1, limit + 1):
                if i + k > n:
                    break
                
                cost += abs(robot[i + k - 1] - pos)
                res = min(res, cost + dp(i + k, j + 1))
            
            memo[(i, j)] = res
            return res
        
        return dp(0, 0)
