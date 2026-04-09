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

        # For each small k:
        # events[k][rem] stores multiplicative range events on the sequence
        # rem, rem+k, rem+2k, ...
        events = [None] * B
        for k in range(1, B):
            events[k] = defaultdict(list)

        # Process queries
        for l, r, k, v in queries:
            if k < B:
                rem = l % k
                start = l // k
                end = r // k

                events[k][rem].append((start, v))
                events[k][rem].append((end + 1, pow(v, MOD - 2, MOD)))
            else:
                i = l
                while i <= r:
                    nums[i] = (nums[i] * v) % MOD
                    i += k

        # Apply all small-k lazy updates
        for k in range(1, B):
            for rem, evs in events[k].items():
                evs.sort()
                cur = 1
                p = 0
                m = 0
                idx = rem

                while idx < n:
                    while p < len(evs) and evs[p][0] == m:
                        cur = (cur * evs[p][1]) % MOD
                        p += 1
                    nums[idx] = (nums[idx] * cur) % MOD
                    idx += k
                    m += 1

        ans = 0
        for x in nums:
            ans ^= x
        return ans
