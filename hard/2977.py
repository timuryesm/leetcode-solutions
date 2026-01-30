class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        n = len(source)

        # Group all strings by length, build index maps
        by_len = {}
        def add_str(s):
            L = len(s)
            if L not in by_len:
                by_len[L] = {}
            if s not in by_len[L]:
                by_len[L][s] = len(by_len[L])

        for a, b in zip(original, changed):
            add_str(a)
            add_str(b)

        # Floyd-Warshall per length to get min conversion cost between any two strings
        dist_by_len = {}
        for L, mp in by_len.items():
            m = len(mp)
            dist = [[INF] * m for _ in range(m)]
            for i in range(m):
                dist[i][i] = 0
            dist_by_len[L] = dist

        for a, b, w in zip(original, changed, cost):
            L = len(a)
            ia = by_len[L][a]
            ib = by_len[L][b]
            if w < dist_by_len[L][ia][ib]:
                dist_by_len[L][ia][ib] = w

        for L, dist in dist_by_len.items():
            m = len(dist)
            for k in range(m):
                dk = dist[k]
                for i in range(m):
                    dik = dist[i][k]
                    if dik >= INF:
                        continue
                    di = dist[i]
                    nd_base = dik
                    for j in range(m):
                        nd = nd_base + dk[j]
                        if nd < di[j]:
                            di[j] = nd

        # Trie for matching ORIGINAL strings in source
        trie = {"n": {}, "end": []}  # end holds (L, original_string)
        for s in original:
            node = trie
            for ch in s:
                node = node["n"].setdefault(ch, {"n": {}, "end": []})
            node["end"].append((len(s), s))

        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] >= INF:
                continue

            # Keep one char if already equal
            if source[i] == target[i]:
                if dp[i] < dp[i + 1]:
                    dp[i + 1] = dp[i]

            # Try replacements starting at i (must match an original pattern)
            node = trie
            j = i
            while j < n and source[j] in node["n"]:
                node = node["n"][source[j]]
                j += 1
                if node["end"]:
                    for L, orig_str in node["end"]:
                        end = i + L
                        if end > n:
                            continue
                        tgt_str = target[i:end]
                        mp = by_len.get(L)
                        if mp is None:
                            continue
                        if tgt_str not in mp:
                            continue
                        d = dist_by_len[L][mp[orig_str]][mp[tgt_str]]
                        if d < INF and dp[i] + d < dp[end]:
                            dp[end] = dp[i] + d

        return -1 if dp[n] >= INF else dp[n]
