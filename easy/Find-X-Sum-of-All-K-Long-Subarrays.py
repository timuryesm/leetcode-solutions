class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            # Count frequencies in the current window
            freq = {}
            for j in range(i, i + k):
                v = nums[j]
                freq[v] = freq.get(v, 0) + 1

            # Pick top x by frequency, tie-broken by larger value
            top = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))

            # Sum value * count over the selected elements
            total = 0
            for idx, (val, cnt) in enumerate(top):
                if idx == x:
                    break
                total += val * cnt

            ans.append(total)

            # Note: If distinct < x, we summed all entries, which equals
            # the window sum as required.
        return ans
