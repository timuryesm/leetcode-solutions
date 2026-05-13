class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
        n = len(nums)
        
        # Difference array for range updates
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b)
            high = max(a, b)
            s = a + b

            # Initially assume 2 moves for every sum
            diff[2] += 2

            # For sums in [low+1, high+limit], only 1 move needed
            diff[low + 1] -= 1
            diff[high + limit + 1] += 1

            # For exact sum s, 0 moves needed
            diff[s] -= 1
            diff[s + 1] += 1

        ans = float('inf')
        current = 0

        # Possible sums range from 2 to 2*limit
        for target in range(2, 2 * limit + 1):
            current += diff[target]
            ans = min(ans, current)

        return ans
