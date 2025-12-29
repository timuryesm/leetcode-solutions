from collections import defaultdict

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        nxt = defaultdict(list)
        for pat in allowed:
            nxt[pat[:2]].append(pat[2])

        bad = set()  # rows that cannot lead to a valid pyramid

        def can_build(row):
            if len(row) == 1:
                return True
            if row in bad:
                return False

            # build all possible next rows using backtracking
            candidates = []

            def build_next(i, path):
                if i == len(row) - 1:
                    candidates.append("".join(path))
                    return
                pair = row[i:i+2]
                if pair not in nxt:
                    return
                for ch in nxt[pair]:
                    path.append(ch)
                    build_next(i + 1, path)
                    path.pop()

            build_next(0, [])

            for nr in candidates:
                if can_build(nr):
                    return True

            bad.add(row)
            return False

        return can_build(bottom)
