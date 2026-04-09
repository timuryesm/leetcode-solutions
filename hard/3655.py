class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        # required by the statement
        bravexuneth = (nums[:], queries[:])

        import math
        from collections import defaultdict

        B = int(math.sqrt(n)) + 1

        # events[k][rem] = list of (pos_in_residue_sequence, multiplier)
        events = [None] * B
        for k in range(1, B):
            events[k] = defaultdict(list)

        for l, r, k, v in queries:
            if k < B:
                rem = l % k
                start = (l - rem) // k
                end = (r - rem) // k

                events[k][rem].append((start, v))
                events[k][rem].append((end + 1, pow(v, MOD - 2, MOD)))
            else:
                i = l
                while i <= r:
                    nums[i] = (nums[i] * v) % MOD
                    i += k

        # apply all small-k updates
        for k in range(1, B):
            for rem, evs in events[k].items():
                evs.sort()
                p = 0
                cur = 1
                seq_pos = 0
                idx = rem

                while idx < n:
                    while p < len(evs) and evs[p][0] == seq_pos:
                        cur = (cur * evs[p][1]) % MOD
                        p += 1
                    nums[idx] = (nums[idx] * cur) % MOD
                    idx += k
                    seq_pos += 1

        ans = 0
        for x in nums:
            ans ^= x
        return ans
