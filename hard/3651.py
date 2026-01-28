import heapq
import bisect

class Solution(object):
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        V = m * n
        INF = 10**30

        vals = [0] * V
        for i in range(m):
            for j in range(n):
                vals[i * n + j] = grid[i][j]

        order = sorted(range(V), key=lambda idx: vals[idx])
        sorted_vals = [vals[idx] for idx in order]

        def idx_to_rc(idx):
            return divmod(idx, n)

        dist = [[INF] * V for _ in range(k + 1)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # (cost, used_tele, cell_idx)

        # DSU "next unprocessed" per teleport-layer (1..k)
        parent = []
        for _ in range(k + 1):
            p = list(range(V + 1))
            parent.append(p)

        def find(layer, x):
            p = parent[layer]
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x

        while pq:
            d, t, u = heapq.heappop(pq)
            if d != dist[t][u]:
                continue

            if u == V - 1:
                # can't early-exit because maybe reach with fewer teleports already minimal,
                # but Dijkstra order ensures this is minimal for this state.
                pass

            i, j = idx_to_rc(u)

            # normal moves
            if j + 1 < n:
                v = u + 1
                nd = d + grid[i][j + 1]
                if nd < dist[t][v]:
                    dist[t][v] = nd
                    heapq.heappush(pq, (nd, t, v))
            if i + 1 < m:
                v = u + n
                nd = d + grid[i + 1][j]
                if nd < dist[t][v]:
                    dist[t][v] = nd
                    heapq.heappush(pq, (nd, t, v))

            # teleport (0 cost) to any cell with value <= current value
            if t < k:
                layer = t + 1
                limit = bisect.bisect_right(sorted_vals, vals[u])
                x = find(layer, 0)
                while x < limit:
                    v = order[x]
                    if d < dist[layer][v]:
                        dist[layer][v] = d
                        heapq.heappush(pq, (d, layer, v))
                    parent[layer][x] = find(layer, x + 1)
                    x = find(layer, x)

        ans = min(dist[t][V - 1] for t in range(k + 1))
        return -1 if ans >= INF else ans
