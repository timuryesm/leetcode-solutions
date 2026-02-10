class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for l in range(n):
            even_set, odd_set = set(), set()
            even_cnt = odd_cnt = 0

            for r in range(l, n):
                x = nums[r]
                if x & 1:
                    if x not in odd_set:
                        odd_set.add(x)
                        odd_cnt += 1
                else:
                    if x not in even_set:
                        even_set.add(x)
                        even_cnt += 1

                if even_cnt == odd_cnt:
                    ans = max(ans, r - l + 1)

        return ans
