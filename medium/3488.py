from collections import defaultdict
import bisect

class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        # Step 1: map value -> indices
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        # Step 2: precompute answer for each index
        res = [-1] * n
        
        for v in pos:
            indices = pos[v]
            if len(indices) == 1:
                continue
            
            m = len(indices)
            for i in range(m):
                cur = indices[i]
                prev = indices[(i - 1) % m]
                nxt = indices[(i + 1) % m]
                
                d1 = abs(cur - prev)
                d2 = abs(cur - nxt)
                
                # circular distance
                d1 = min(d1, n - d1)
                d2 = min(d2, n - d2)
                
                res[cur] = min(d1, d2)
        
        # Step 3: answer queries
        return [res[q] for q in queries]
