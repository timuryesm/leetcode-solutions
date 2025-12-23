import bisect

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # Sort by start time
        events.sort(key=lambda x: x[0])
        n = len(events)

        starts = [e[0] for e in events]

        # suffix_max[i] = max value among events[i..n-1]
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        ans = 0

        for i in range(n):
            s, e, v = events[i]
            ans = max(ans, v)  # take only this event

            # Find first event that starts after this one ends (inclusive ends => need e+1)
            j = bisect.bisect_left(starts, e + 1)
            ans = max(ans, v + suffix_max[j])

        return ans
