class Solution(object):
    def maxStability(self, n, edges, k):
        
        class DSU:
            def __init__(self, n):
                self.p = list(range(n))
            def find(self, x):
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]
            def union(self, a, b):
                pa, pb = self.find(a), self.find(b)
                if pa == pb:
                    return False
                self.p[pa] = pb
                return True
        
        def can(x):
            dsu = DSU(n)
            upgrades = k
            used = 0
            
            # mandatory edges
            for u,v,s,m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if not dsu.union(u,v):
                        return False
                    used += 1
            
            optional = []
            for u,v,s,m in edges:
                if m == 0:
                    optional.append((u,v,s))
            
            # try edges without upgrade
            for u,v,s in optional:
                if s >= x and dsu.union(u,v):
                    used += 1
            
            # try edges with upgrade
            for u,v,s in optional:
                if used == n-1:
                    break
                if s < x and s*2 >= x and upgrades > 0:
                    if dsu.union(u,v):
                        upgrades -= 1
                        used += 1
            
            return used == n-1
        
        lo, hi = 1, max(s for _,_,s,_ in edges) * 2
        ans = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
