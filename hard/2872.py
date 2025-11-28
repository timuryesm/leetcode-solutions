import sys
sys.setrecursionlimit(10**7)

class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        # Build adjacency list
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        self.ans = 0
        
        def dfs(u, parent):
            # compute subtree sum mod k
            sub = values[u] % k
            for v in g[u]:
                if v == parent:
                    continue
                child_rem = dfs(v, u)
                sub = (sub + child_rem) % k
            # If subtree sum divisible by k, it's a component
            if sub % k == 0:
                self.ans += 1
                return 0  # no remainder passed up
            return sub
        
        dfs(0, -1)
        return self.ans
