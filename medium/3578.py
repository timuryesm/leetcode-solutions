from collections import deque

class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # dp[i] = number of ways to partition nums[0..i-1]
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # prefix sums: pre[i] = dp[0] + ... + dp[i]
        pre = [0] * (n + 1)
        pre[0] = dp[0]
        
        maxDeque = deque()  # indices in decreasing nums[]
        minDeque = deque()  # indices in increasing nums[]
        
        l = 0  # left pointer for sliding window
        
        for j in range(0, n):
            # Maintain maxDeque (decreasing)
            while maxDeque and nums[maxDeque[-1]] <= nums[j]:
                maxDeque.pop()
            maxDeque.append(j)
            
            # Maintain minDeque (increasing)
            while minDeque and nums[minDeque[-1]] >= nums[j]:
                minDeque.pop()
            minDeque.append(j)
            
            # Shrink from left while max - min > k
            while maxDeque and minDeque and nums[maxDeque[0]] - nums[minDeque[0]] > k:
                if maxDeque[0] == l:
                    maxDeque.popleft()
                if minDeque[0] == l:
                    minDeque.popleft()
                l += 1
            
            # Now window [l..j] is minimal valid window ending at j.
            # Segments [s..j] are valid for all s in [l, j].
            if l == 0:
                ways = pre[j]  # sum dp[0..j]
            else:
                ways = (pre[j] - pre[l - 1]) % MOD  # sum dp[l..j]
            
            dp[j + 1] = ways % MOD
            pre[j + 1] = (pre[j] + dp[j + 1]) % MOD
        
        return dp[n]
