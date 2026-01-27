import heapq

class Solution(object):
    def minCost(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))         # normal move
            adj[v].append((u, 2 * w))     # reverse this incoming edge at v and traverse

        INF = 10**30
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)

        while pq:
            d, x = heapq.heappop(pq)
            if d != dist[x]:
                continue
            if x == n - 1:
                return d
            for y, w in adj[x]:
                nd = d + w
                if nd < dist[y]:
                    dist[y] = nd
                    heapq.heappush(pq, (nd, y))

        return -1
