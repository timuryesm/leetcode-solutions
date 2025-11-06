import heapq

class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # --- DSU (Union-Find) to build static connected components ---
        parent = [i for i in range(c + 1)]
        rank = [0] * (c + 1)

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for u, v in connections:
            union(u, v)

        # Final component id for each station (static)
        comp_of = [0] * (c + 1)
        for i in range(1, c + 1):
            comp_of[i] = find(i)

        # --- Per-component min-heaps of member station IDs ---
        heaps = [[] for _ in range(c + 1)]
        for i in range(1, c + 1):
            heaps[comp_of[i]].append(i)
        for r in range(1, c + 1):
            if heaps[r]:
                heapq.heapify(heaps[r])

        # Online status (initially all True)
        online = [False] * (c + 1)
        for i in range(1, c + 1):
            online[i] = True

        ans = []

        # Helper to get smallest online id in a component
        def smallest_online(root):
            h = heaps[root]
            while h and not online[h[0]]:
                heapq.heappop(h)
            return h[0] if h else -1

        # --- Process queries ---
        for t, x in queries:
            if t == 1:
                if online[x]:
                    ans.append(x)
                else:
                    root = comp_of[x]
                    ans.append(smallest_online(root))
            else:  # t == 2 -> take station offline
                if online[x]:
                    online[x] = False
                # (If already offline, nothing to do)

        return ans
